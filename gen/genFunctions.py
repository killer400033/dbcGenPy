import config
from gen import genSignals, helpers

def generateUnpackCode(message):
    function_code = f"// Unpack signals from {message.name}\n"
    function_code += f"int8_t Unpack_{message.name}({message.name}_t* _m, const uint8_t* _d, uint8_t len) {{\n"

    function_code += f"\tif (len < {message.length}u) return STATUS_ERROR;\n\n"

    for signal in message.signals:
        function_code += genSignals.generateSignalCode(signal, "_m")
    
    function_code += "\n\treturn STATUS_OK;\n"
    function_code += "}\n\n"

    return function_code

def generateFunctionPrototypes(message):
    prototypecode = f"int8_t Unpack_{message.name}({message.name}_t* _m, const uint8_t* _d, uint8_t len);\n"

    return prototypecode

# Given a can signal, generates the macros for offset and scaling
def generateMacros(message):
    macroCode = ""
    for signal in message.signals:
        if helpers.shouldUseSigFloat(signal):
            macroCode += f"#define {config.SCALE_OFFSET_PREFIX}{signal.name.upper()}(x) "
            precision = config.FLOAT_LITERAL_PREC
            macroCode += f"( (((x) * ({float(signal.scale):.{precision}f})) + ({float(signal.offset):.{precision}f})) );\n"
            
    return macroCode