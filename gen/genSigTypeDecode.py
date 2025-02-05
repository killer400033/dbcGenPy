from gen import helpers
import config

def generateSignalTypeDecodeFunc(message):
    code = ""
    for signal in message.signals:
        data_type = helpers.getSignalDataType(signal, overwrite_sigfloat=True)
        non_sigfloat_data_type = helpers.getSignalDataType(signal, overwrite_sigfloat=False)
        code += f"{data_type} Decode_i{message.frame_id}_{signal.name}_Type(uint64_t signal) {{\n"
        if helpers.shouldUseSigFloat(signal, overwrite_sigfloat=True):
            code += f"\treturn ({config.SIGFLOAT_TYPE}){config.UNPACK_SCALE_OFFSET_PREFIX}{message.name.upper()}_{signal.name.upper()}(({non_sigfloat_data_type})signal);\n"
        else:
            code += f"\treturn ({data_type})signal;\n"
        code += "}\n\n"
    return code

def generateSignalTypeDecodeFuncPrototypes(message):
    code = ""
    for signal in message.signals:
        data_type = helpers.getSignalDataType(signal, overwrite_sigfloat=True)
        code += f"{data_type} Decode_i{message.frame_id}_{signal.name}_Type(uint64_t signal);\n"
    return code

def generateSignalTypeEncodeFunc(message):
    code = ""
    for signal in message.signals:
        data_type = helpers.getSignalDataType(signal, overwrite_sigfloat=True)
        encoded_data_type = helpers.getUnsignedSignalDataType(signal)
        code += f"{encoded_data_type} Encode_i{message.frame_id}_{signal.name}_Type({data_type} signal) {{\n"
        if helpers.shouldUseSigFloat(signal, overwrite_sigfloat=True):
            code += f"\treturn ({encoded_data_type}){config.PACK_SCALE_OFFSET_PREFIX}{message.name.upper()}_{signal.name.upper()}(signal);\n"
        else:
            code += f"\treturn ({encoded_data_type})signal;\n"
        code += "}\n\n"
    return code

def generateSignalTypeEncodeFuncPrototypes(message):
    code = ""
    for signal in message.signals:
        data_type = helpers.getSignalDataType(signal, overwrite_sigfloat=True)
        encoded_data_type = helpers.getUnsignedSignalDataType(signal)
        code += f"{encoded_data_type} Encode_i{message.frame_id}_{signal.name}_Type({data_type} signal);\n"
    return code