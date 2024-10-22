import config
from gen import genSignals

def generateUnpackCode(message):
    remainingStart = 0
    function_code = f"// Unpack signals from {message.name}\n"
    function_code += f"uint8_t Unpack_{message.name}({message.name}_t* _m, const uint8_t* _d, uint8_t len) {{\n"

    function_code += f"\tif (len < {message.length}u) return -1;\n\n"

    for signal in message.signals:
        function_code += genSignals.generateSignalCode(signal, "_m")
    
    function_code += "\n\treturn 0;\n"
    function_code += "}\n\n"

    return function_code