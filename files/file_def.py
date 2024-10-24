import config
import os
from files.class_def import SourceFile, HeaderFile
from gen import genFunctions, genStructs, genUnits, genEnums, genValDecode

# Different file implementations
class MainSourceFile(SourceFile):
    def __init__(self):
        self.filename = config.MAIN_NAME
        self.usercodes = []

    def generateContent(self, f, db, user_code_content):
        f.write(f"#include \"{self.filename}.h\"\n\n")

        for message in db.messages:
            code = genFunctions.generateUnpackCode(message)
            f.write(code)


class MainHeaderFile(HeaderFile):
    def __init__(self):
        self.filename = config.MAIN_NAME
        self.usercodes = []
    
    def generateContent(self, f, db, user_code_content):
        f.write(f"#include \"{self.filename}.h\"\n\n")

        f.write("#include <stdint.h>\n\n")

        f.write(f"typedef {config.SIGFLOAT_TYPE} sigfloat_t;\n\n")
        f.write(f"#define STATUS_OK 0\n")
        f.write(f"#define STATUS_ERROR -1\n\n")
        
        for message in db.messages:
            code = genStructs.generateStructsCode(message)
            f.write(code)

        f.write("\n// Unpack function prototypes\n")

        for message in db.messages:
            code = genFunctions.generateFunctionPrototypes(message)
            f.write(code)
        
        f.write("\n// Macros to apply scaling and offset\n")

        for message in db.messages:
            code = genFunctions.generateMacros(message)
            f.write(code)


class SigUnitsHeaderFile(HeaderFile):
    def __init__(self):
        self.filename = config.SIGNAL_UNITS_NAME
        self.usercodes = ['custom units']

    def generateContent(self, f, db, user_code_content):
        f.write("// All the units used by the different signals\n")
        for message in db.messages:
            code = genUnits.generateUnitCode(message)
            f.write(code)
        
        f.write(getUserCodeContent(user_code_content, 'custom units'))


class SigEnumsHeaderFile(HeaderFile):
    def __init__(self):
        self.filename = config.SIGNAL_ENUMS_NAME
        self.usercodes = ['custom signals']

    def generateContent(self, f, db, user_code_content):
        f.write("// Enum of every signal in every message\n")
        f.write("typedef enum signal_enum {{\n")

        f.write("// All the units used by the different signals\n")
        for message in db.messages:
            code = genEnums.generateEnumCode(message)
            f.write(code)

        f.write(getUserCodeContent(user_code_content, 'custom signals'))

        f.write("} signal_id_t;\n")


class SigValsSourceFile(SourceFile):
    def __init__(self):
        self.filename = config.SIGNAL_VALS_NAME
        self.usercodes = ['custom decode functions']

    def generateContent(self, f, db, user_code_content):
        f.write(f"#include <string.h>\n")
        f.write(f"#include \"{self.filename}.h\"\n\n")

        for message in db.messages:
            code = genValDecode.generateValDecodeFunctions(message)
            f.write(code)

        f.write(getUserCodeContent(user_code_content, 'custom decode functions'))


class SigValsHeaderFile(HeaderFile):
    def __init__(self):
        self.filename = config.SIGNAL_VALS_NAME
        self.usercodes = ['custom val defines', 'custom decode functions']

    def generateContent(self, f, db, user_code_content):
        f.write("#include <stdint.h>\n\n")
        f.write("\n// String values of signals\n")
        for message in db.messages:
            code = genValDecode.generateValDefines(message)
            f.write(code)
        
        f.write(getUserCodeContent(user_code_content, 'custom val defines'))
        
        f.write("\n\n// Function prototypes for getting val from signal\n")
        for message in db.messages:
            code = genValDecode.generateValDecodeFuncPrototypes(message)
            f.write(code)

        f.write(getUserCodeContent(user_code_content, 'custom function prototypes'))


def getUserCodeContent(user_code_content, name):
    code = f'/* USER CODE BEGIN {name} */\n'
    code += user_code_content.get(name, '')
    code += f'/* USER CODE END {name} */\n'
    return code