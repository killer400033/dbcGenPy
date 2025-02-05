import config
import os
from files.class_def import SourceFile, HeaderFile
from gen import genFunctions, genStructs, genUnits, genEnums, genValDecode, genSigTypeDecode

# Different file implementations
class MainSourceFile(SourceFile):
    def __init__(self):
        self.filename = config.MAIN_NAME
        self.usercodes = []

    def generateContent(self, f, messages, user_code_content):
        f.write(f"#include \"{self.filename}.h\"\n\n")
        
        if config.GENERATE_UNPACK:
            for message in messages:
                code = genFunctions.generateUnpackCode(message)
                f.write(code)

        if config.GENERATE_PACK:
            for message in messages:
                code = genFunctions.generatePackCode(message)
                f.write(code)


class MainHeaderFile(HeaderFile):
    def __init__(self):
        self.filename = config.MAIN_NAME
        self.usercodes = []
    
    def generateContent(self, f, messages, user_code_content):
        f.write(f"#include \"{self.filename}.h\"\n\n")

        f.write("#include <stdint.h>\n\n")

        f.write(f"#define STATUS_OK 0\n")
        f.write(f"#define STATUS_ERROR -1\n\n")
        
        for message in messages:
            code = genStructs.generateStructsCode(message)
            f.write(code)

        if config.GENERATE_UNPACK:
            f.write("\n// Unpack function prototypes\n")
            for message in messages:
                code = genFunctions.generateUnpackFunctionPrototypes(message)
                f.write(code)

        if config.GENERATE_PACK:
            f.write("\n// Pack function prototypes\n")
            for message in messages:
                code = genFunctions.generatePackFunctionPrototypes(message)
                f.write(code)
        
        f.write("\n// Macros to apply scaling and offset\n")
        for message in messages:
            code = genFunctions.generateMacros(message)
            f.write(code)


class SigUnitsHeaderFile(HeaderFile):
    def __init__(self):
        self.filename = config.SIGNAL_UNITS_NAME
        self.usercodes = ['custom units']

    def generateContent(self, f, messages, user_code_content):
        f.write("// All the units used by the different signals\n")
        for message in messages:
            code = genUnits.generateUnitCode(message)
            f.write(code)
        
        f.write(getUserCodeContent(user_code_content, 'custom units'))


class SigEnumsHeaderFile(HeaderFile):
    def __init__(self):
        self.filename = config.SIGNAL_ENUMS_NAME
        self.usercodes = ['custom signals']

    def generateContent(self, f, messages, user_code_content):
        f.write("// Enum of every signal in every message\n")
        f.write("typedef enum signal_enum {\n")

        for message in messages:
            code = genEnums.generateEnumCode(message)
            f.write(code)

        f.write(getUserCodeContent(user_code_content, 'custom signals'))

        f.write("} signal_id_t;\n")

class SigValsHeaderFile(HeaderFile):
    def __init__(self):
        self.filename = config.SIGNAL_VALS_NAME
        self.usercodes = ['custom val defines']

    def generateContent(self, f, messages, user_code_content):
        f.write("#include <stdint.h>\n\n")
        f.write("\n// Value mapping of signals\n")
        for message in messages:
            code = genValDecode.generateValDefines(message)
            f.write(code)
        
        f.write(getUserCodeContent(user_code_content, 'custom val defines'))


class SigTypeDecodeSourceFile(SourceFile):
    def __init__(self):
        self.filename = config.SIGNAL_TYPE_DECODE_NAME
        self.usercodes = []

    def generateContent(self, f, messages, user_code_content):
        f.write(f"#include \"{self.filename}.h\"\n")
        f.write(f"#include \"{config.MAIN_NAME}.h\"\n\n")
        f.write("// These function, given the signal in uint64_t form, returns their correct type with offset/scale applied\n\n")
        for message in messages:
            code = genSigTypeDecode.generateSignalTypeDecodeFunc(message)
            f.write(code)

        f.write("// These function, given the signal in the decoded form, undoes the offset/scale and returns the encoded value\n\n")
        for message in messages:
            code = genSigTypeDecode.generateSignalTypeEncodeFunc(message)
            f.write(code)

class SigTypeDecodeHeaderFile(HeaderFile):
    def __init__(self):
        self.filename = config.SIGNAL_TYPE_DECODE_NAME
        self.usercodes = []

    def generateContent(self, f, messages, user_code_content):
        f.write("#include <stdint.h>\n\n")
        f.write("// Function prototypes for decoding signal value\n\n")
        for message in messages:
            code = genSigTypeDecode.generateSignalTypeDecodeFuncPrototypes(message)
            f.write(code)

    def generateContent(self, f, messages, user_code_content):
        f.write("#include <stdint.h>\n\n")
        f.write("// Function prototypes for encoding signal value\n\n")
        for message in messages:
            code = genSigTypeDecode.generateSignalTypeEncodeFuncPrototypes(message)
            f.write(code)


def getUserCodeContent(user_code_content, name):
    code = f'\n/* USER CODE BEGIN {name} */'
    content = user_code_content.get(name, '')
    code += '\n' if content == '' else content
    code += f'/* USER CODE END {name} */\n'
    return code