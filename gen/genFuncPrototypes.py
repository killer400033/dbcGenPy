def generateFunctionPrototypes(message):
    prototypecode = f"int8_t Unpack_{message.name}({message.name}_t* _m, const uint8_t* _d, uint8_t len);\n"

    return prototypecode