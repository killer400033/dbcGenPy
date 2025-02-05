import config
from typing import Iterator, Tuple
from gen import helpers

def generateSignalUnpackCode(signal, structInstance):
    signalcode = f"\t// Extracting {signal.name}\n"
    if helpers.shouldUseSigFloat(signal):
        signalcode += f"\t{structInstance}->{signal.name} = ({config.SIGFLOAT_TYPE}){config.UNPACK_SCALE_OFFSET_PREFIX}{signal.name.upper()}({generateDataUnpackCode(signal)});\n"
    else:
        signalcode += f"\t{structInstance}->{signal.name} = {generateDataUnpackCode(signal)};\n"
    return signalcode

def generateDataUnpackCode(signal):
    datacode = ""
    for i, (index, shift, shift_dir, mask) in enumerate(getSegments(signal, True)):
        if i != 0: datacode += " | "

        if (shift_dir == 'left'):
            datacode += f"((_d[{index}] & 0x{mask:02x}u) << {shift}u)"
        elif (shift_dir == 'right'):
            datacode += f"((_d[{index}] & 0x{mask:02x}u) >> {shift}u)"
    return datacode

def generateSignalPackCode(signal, structInstance):
    datacode = ""
    for i, (index, shift, shift_dir, mask) in enumerate(getSegments(signal, False)):
        sigval = ""
        if helpers.shouldUseSigFloat(signal):
            sigval = f"(({helpers.getUnsignedSignalDataType(signal)}){config.UNPACK_SCALE_OFFSET_PREFIX}{signal.name.upper()}({structInstance}->{signal.name}))"
        else:
            sigval = f"(({helpers.getUnsignedSignalDataType(signal)})({structInstance}->{signal.name}))"

        if (shift_dir == 'left'):
            datacode += f"\t_d[{index}] |= (( {sigval} << {shift}u) & 0x{mask:02x}u);\n"
        elif (shift_dir == 'right'):
            datacode += f"\t_d[{index}] |= (( {sigval} >> {shift}u) & 0x{mask:02x}u);\n"
    return datacode

# Code from cantools library. Refer to its source code for this function
def getSegments(signal, invert_shift: bool) -> Iterator[Tuple[int, int, str, int]]:
    index, pos = divmod(signal.start, 8)
    left = signal.length

    while left > 0:
        if signal.byte_order == 'big_endian':
            if left >= (pos + 1):
                length = (pos + 1)
                pos = 7
                shift = -(left - length)
                mask = ((1 << length) - 1)
            else:
                length = left
                shift = (pos - length + 1)
                mask = ((1 << length) - 1)
                mask <<= (pos - length + 1)
        else:
            shift = (left - signal.length) + pos

            if left >= (8 - pos):
                length = (8 - pos)
                mask = ((1 << length) - 1)
                mask <<= pos
                pos = 0
            else:
                length = left
                mask = ((1 << length) - 1)
                mask <<= pos

        if invert_shift:
            if shift < 0:
                shift = -shift
                shift_direction = 'left'
            else:
                shift_direction = 'right'
        else:
            if shift < 0:
                shift = -shift
                shift_direction = 'right'
            else:
                shift_direction = 'left'

        yield index, shift, shift_direction, mask

        left -= length
        index += 1