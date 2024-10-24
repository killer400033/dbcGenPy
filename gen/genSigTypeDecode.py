from gen import helpers
import config

def generateSignalTypeDecodeFunc(message):
    code = ""
    for signal in message.signals:
        data_type = helpers.getSignalDataType(signal, force_use_sigfloat=True)
        code += f"{data_type} Decode_{signal.name}_Type(uint64_t signal) {{\n"
        if helpers.shouldUseSigFloat(force_use_sigfloat=True):
            code += f"return {config.SCALE_OFFSET_PREFIX}{config.SCALE_OFFSET_PREFIX}{signal.name.upper()}(signal)\n"
        else:
            code += f"return ({data_type})signal;\n"
        code += "}\n\n"
    return code

def generateSignalTypeDecodeFuncPrototypes(message):
    code = ""
    for signal in message.signals:
        data_type = helpers.getSignalDataType(signal, force_use_sigfloat=True)
        code += f"{data_type} Decode_{signal.name}_Type(uint64_t signal);\n"
    return code