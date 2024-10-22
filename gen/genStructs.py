import config

# Given a can frame/message, generates the struct that contains all its signals
def generateStructsCode(message):
    structCode = f"// Struct for {message.name}\n"
    structCode += f"typedef struct {{\n"
    for signal in message.signals:
        length = signal.length
        signed = signal.is_signed
        scale = signal.scale
        offset = signal.offset
        
        if (scale != 1 or offset != 0) and config.USE_SIGFLOAT:
            data_type = config.SIGFLOAT_TYPE
        else:
            if signed:
                if length <= 8:
                    data_type = "int8_t"
                elif length <= 16:
                    data_type = "int16_t"
                elif length <= 32:
                    data_type = "int32_t"
                else:
                    data_type = "int64_t"
            else:
                if length <= 8:
                    data_type = "uint8_t"
                elif length <= 16:
                    data_type = "uint16_t"
                elif length <= 32:
                    data_type = "uint32_t"
                else:
                    data_type = "uint64_t"
        
        structCode += f"\t{data_type} {signal.name};\n"
            
    structCode += f"}} {message.name}_t;\n\n"
    return structCode 
            