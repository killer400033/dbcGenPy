import cantools
import os
from gen import genFunctions, genStructs, genMacros, genUnits, genEnums, genFuncPrototypes
import config
import sys
import shutil

if len(sys.argv) > 1:
    os.chdir(sys.argv[1])

dbc_file_path = config.DBC_DIR
try:
    db = cantools.database.load_file(dbc_file_path)
except Exception as e:
    sys.stderr.write(f"{e}\n")
    sys.exit(1)

# Remove old files
def recreate_directory(dir_path):
    if os.path.exists(dir_path):
        shutil.rmtree(dir_path)
    os.makedirs(dir_path)
    print(f"Cleared {dir_path}")

recreate_directory(config.SOURCE_OUT_DIR)
recreate_directory(config.HEADER_OUT_DIR)

# Main c file
file_path = os.path.join(config.SOURCE_OUT_DIR, f"{config.OUT_NAME}.c")
with open(file_path, 'w') as f:
    f.write(f"#include \"{config.OUT_NAME}.h\"\n\n")

    for message in db.messages:
        code = genFunctions.generateUnpackCode(message)
        f.write(code)
        
    print(f"Generated {config.OUT_NAME}.c")


# Main header file
file_path = os.path.join(config.HEADER_OUT_DIR, f"{config.OUT_NAME}.h")
with open(file_path, 'w') as f:
    f.write("#include <stdint.h>\n\n")

    f.write(f"typedef {config.SIGFLOAT_TYPE} sigfloat_t;\n\n")
    f.write(f"#define STATUS_OK 0\n")
    f.write(f"#define STATUS_ERROR -1\n\n")
    
    for message in db.messages:
        code = genStructs.generateStructsCode(message)
        f.write(code)

    f.write("\n// Unpack function prototypes\n")

    for message in db.messages:
        code = genFuncPrototypes.generateFunctionPrototypes(message)
        f.write(code)
    
    f.write("\n// Macros to apply scaling and offset\n")

    for message in db.messages:
        code = genMacros.generateMacros(message)
        f.write(code)
    print(f"Generated {config.OUT_NAME}.h")

# units header file
if config.GENERATE_UNITS:
    file_path = os.path.join(config.HEADER_OUT_DIR, "units.h")
    with open(file_path, 'w') as f:
        for message in db.messages:
            code = genUnits.generateUnitCode(message)
            f.write(code)
        print(f"Generated units.h")

if config.GENERATE_ENUMS:
    file_path = os.path.join(config.HEADER_OUT_DIR, "enums.h")
    with open(file_path, 'w') as f:
        for message in db.messages:
            code = genEnums.generateEnumCode(message)
            f.write(code)
        print(f"Generated enums.h")

