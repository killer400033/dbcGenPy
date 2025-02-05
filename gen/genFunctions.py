import config
from gen import genSignals, helpers

def generateUnpackCode(message):
    function_code = f"// Unpack signals from {message.name}\n"
    function_code += f"int8_t Unpack_{message.name}({message.name}_t* _m, const uint8_t* _d, uint8_t len) {{\n"

    function_code += f"\tif (len < {message.length}u) return STATUS_ERROR;\n\n"

    for signal in message.signals:
        function_code += genSignals.generateSignalUnpackCode(signal, "_m")
    
    function_code += "\n\treturn STATUS_OK;\n"
    function_code += "}\n\n"

    return function_code

def generateUnpackFunctionPrototypes(message):
    prototypecode = f"int8_t Unpack_{message.name}({message.name}_t* _m, const uint8_t* _d, uint8_t len);\n"

    return prototypecode

def generatePackCode(message):
    function_code = f"// Pack signals from {message.name}\n"
    function_code += f"int8_t Pack_{message.name}(const {message.name}_t* _m, uint8_t* _d, uint8_t len) {{\n"

    function_code += f"\tif (len < {message.length}u) return STATUS_ERROR;\n\n"

    function_code += f"\tfor (uint8_t i = 0u; i < {message.length}u; _d[i++] = {config.BYTE_INIT_VALUE});\n\n"

    for signal in message.signals:
        function_code += genSignals.generateSignalPackCode(signal, "_m")
    
    function_code += "\n\treturn STATUS_OK;\n"
    function_code += "}\n\n"

    return function_code

def generatePackFunctionPrototypes(message):
    prototypecode = f"int8_t Pack_{message.name}(const {message.name}_t* _m, uint8_t* _d, uint8_t len);\n"

    return prototypecode

# Given a can signal, generates the macros for offset and scaling
def generateMacros(message):
    macroCode = ""
    for signal in message.signals:
        if helpers.shouldUseSigFloat(signal) or config.GENERATE_SIGNAL_TYPE_DECODE:
            macroCode += f"#define {config.UNPACK_SCALE_OFFSET_PREFIX}{signal.name.upper()}(x) "
            precision = config.FLOAT_LITERAL_PREC
            macroCode += f"( (((x) * ({float(signal.scale):.{precision}f})) + ({float(signal.offset):.{precision}f})) );\n"

    for signal in message.signals:
        if helpers.shouldUseSigFloat(signal) or config.GENERATE_SIGNAL_TYPE_DECODE:
            macroCode += f"#define {config.PACK_SCALE_OFFSET_PREFIX}{signal.name.upper()}(x) "
            precision = config.FLOAT_LITERAL_PREC
            macroCode += f"( (((x) - ({float(signal.offset):.{precision}f})) / ({float(signal.scale):.{precision}f})) );\n"
            
    return macroCode