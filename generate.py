import cantools
import os
from files.file_def import MainSourceFile, MainHeaderFile, SigUnitsHeaderFile, SigEnumsHeaderFile, SigValsSourceFile, SigValsHeaderFile
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

# Main source file
MainSourceFile().generate(db)
# Main header file
MainHeaderFile().generate(db)

# Signal units header file
SigUnitsHeaderFile().generate(db)
# Signal enums header file
SigEnumsHeaderFile().generate(db)

# Signal vals source file
SigValsSourceFile().generate(db)
# Signal vals header file
SigValsHeaderFile.generate(db)