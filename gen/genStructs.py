import config
from gen import helpers

# Given a can frame/message, generates the struct that contains all its signals
def generateStructsCode(message):
    structCode = f"// Struct for {message.name}\n"
    structCode += f"typedef struct {{\n"
    for signal in message.signals:        
        data_type = helpers.getSignalDataType(signal)
        
        structCode += f"\t{data_type} {signal.name};\n"
            
    structCode += f"}} {message.name}_t;\n\n"
    return structCode 