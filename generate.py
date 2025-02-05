import cantools
import os
from files.file_def import MainSourceFile, MainHeaderFile, SigUnitsHeaderFile, SigEnumsHeaderFile, SigValsHeaderFile, SigTypeDecodeHeaderFile, SigTypeDecodeSourceFile
import config
import sys
import shutil

if len(sys.argv) > 1:
    os.chdir(sys.argv[1])

messages = []

for dbc_dir in config.DBC_DIRS:
    dbc_file_path = os.path.join(config.DBC_FILE_DIR, dbc_dir)

    try:
        db = cantools.database.load_file(dbc_file_path)
        messages.extend(db.messages)
    except Exception as e:
        sys.stderr.write(f"{e}\n")
        sys.exit(1)

unique_messages = {}
for message in messages:
    unique_messages[message.name] = message

messages = list(unique_messages.values())

# Make sure directories exist
os.makedirs(config.SOURCE_OUT_DIR, exist_ok=True)
os.makedirs(config.HEADER_OUT_DIR, exist_ok=True)

# Main source file
MainSourceFile().generate(messages)
# Main header file
MainHeaderFile().generate(messages)

# Signal units header file
if config.GENERATE_SIGNAL_UNITS:
    SigUnitsHeaderFile().generate(messages)

# Signal enums header file
if config.GENERATE_SIGNAL_ENUMS:
    SigEnumsHeaderFile().generate(messages)

# Signal vals header file
if config.GENERATE_SIGNAL_VALS:
    SigValsHeaderFile().generate(messages)

if config.GENERATE_SIGNAL_TYPE_DECODE:
    # Signal type decode source file
    SigTypeDecodeSourceFile().generate(messages)
    # Signal type decode header file
    SigTypeDecodeHeaderFile().generate(messages)