import cantools
import os
from files.file_def import MainSourceFile, MainHeaderFile, SigUnitsHeaderFile, SigEnumsHeaderFile, SigValsHeaderFile, SigTypeDecodeHeaderFile, SigTypeDecodeSourceFile
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

# Make sure directories exist
os.makedirs(config.SOURCE_OUT_DIR, exist_ok=True)
os.makedirs(config.HEADER_OUT_DIR, exist_ok=True)

# Main source file
MainSourceFile().generate(db)
# Main header file
MainHeaderFile().generate(db)

# Signal units header file
if config.GENERATE_SIGNAL_UNITS:
    SigUnitsHeaderFile().generate(db)

# Signal enums header file
if config.GENERATE_SIGNAL_ENUMS:
    SigEnumsHeaderFile().generate(db)

# Signal vals header file
if config.GENERATE_SIGNAL_VALS:
    SigValsHeaderFile().generate(db)

if config.GENERATE_SIGNAL_TYPE_DECODE:
    # Signal type decode source file
    SigTypeDecodeSourceFile().generate(db)
    # Signal type decode header file
    SigTypeDecodeHeaderFile().generate(db)