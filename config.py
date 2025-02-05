import configparser
import os
import sys

config_path = ".cdonfig"
config = configparser.ConfigParser()

if os.path.exists(config_path):
    config.read(config_path)
    # Convert values from the config file
    USE_SIGFLOAT = config.getboolean("GEN", "USE_SIGFLOAT")
    SIGFLOAT_TYPE = config.get("GEN", "SIGFLOAT_TYPE")
    FLOAT_LITERAL_PREC = config.getint("GEN", "FLOAT_LITERAL_PREC")

    # Options
    GENERATE_PACK = config.getboolean("OPTIONS", "GENERATE_PACK")
    GENERATE_UNPACK = config.getboolean("OPTIONS", "GENERATE_UNPACK")
    GENERATE_SIGNAL_UNITS = config.getboolean("OPTIONS", "GENERATE_SIGNAL_UNITS")
    GENERATE_SIGNAL_ENUMS = config.getboolean("OPTIONS", "GENERATE_SIGNAL_ENUMS")
    GENERATE_SIGNAL_VALS = config.getboolean("OPTIONS", "GENERATE_SIGNAL_VALS")
    GENERATE_SIGNAL_TYPE_DECODE = config.getboolean("OPTIONS", "GENERATE_SIGNAL_TYPE_DECODE")

    # DBC files (stored as a list)
    DBC_DIRS = [
        line.strip() 
        for line in config.get("DBC_FILES", "DBC_DIRS").splitlines() 
        if line.strip() and not line.strip().startswith("#")
    ]

    # File Dirs
    SOURCE_OUT_DIR = config.get("FILE_DIRS", "SOURCE_OUT_DIR")
    HEADER_OUT_DIR = config.get("FILE_DIRS", "HEADER_OUT_DIR")
    DBC_FILE_DIR = config.get("FILE_DIRS", "DBC_FILE_DIR")
else:
    sys.stderr.write(f"Error: The file {config_path} does not exist.\n")
    sys.exit(1)

# Don't change
MAIN_NAME="dbc"
SIGNAL_VALS_NAME="sig_vals"
SIGNAL_UNITS_NAME="sig_units"
SIGNAL_ENUMS_NAME="sig_enum"
SIGNAL_TYPE_DECODE_NAME="sig_type_dec"
UNPACK_SCALE_OFFSET_PREFIX="UNPACK_SCALE_OFFSET_"
PACK_SCALE_OFFSET_PREFIX="PACK_SCALE_OFFSET_"
BYTE_INIT_VALUE="0u"