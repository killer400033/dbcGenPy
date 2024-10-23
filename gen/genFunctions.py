import config
from gen import genSignals

def generateUnpackCode(message):
    function_code = f"// Unpack signals from {message.name}\n"
    function_code += f"int8_t Unpack_{message.name}({message.name}_t* _m, const uint8_t* _d, uint8_t len) {{\n"

    function_code += f"\tif (len < {message.length}u) return STATUS_ERROR;\n\n"

    for signal in message.signals:
        function_code += genSignals.generateSignalCode(signal, "_m")
    
    function_code += "\n\treturn STATUS_OK;\n"
    function_code += "}\n\n"

    return function_code