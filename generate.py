import cantools
import os
from files.file_def import MainSourceFile, MainHeaderFile, SigUnitsHeaderFile, SigEnumsHeaderFile, SigValsHeaderFile, SigTypeDecodeHeaderFile, SigTypeDecodeSourceFile
import config
import sys
import shutil

messages = []
message_sources = {}

for dbc_dir in config.DBC_DIRS:
    dbc_file_path = os.path.join(config.DBC_FILE_DIR, dbc_dir)

    try:
        db = cantools.database.load_file(dbc_file_path)
        for message in db.messages:
            if message.name not in message_sources:
                message_sources[message.name] = [dbc_file_path]
                messages.append(message)
            else:
                message_sources[message.name].append(dbc_file_path)
    except Exception as e:
        sys.stderr.write(f"{e}\n")
        sys.exit(1)

for message_name, file_paths in message_sources.items():
    if len(file_paths) > 1:
        sys.stderr.write(f"Warning: Can Frame '{message_name}' appears multiple times in: {', '.join(file_paths)}\n")

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