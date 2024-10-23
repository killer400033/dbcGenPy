import os

# Code generation settings
USE_SIGFLOAT = True
SIGFLOAT_TYPE = 'double'
FLOAT_LITERAL_PREC = 6 # number of decimal points in generated floating literals

# options
GENERATE_UNITS = False
GENERATE_ENUMS = True
GENERATE_VAL_DECODE = True

# Locations
DBC_DIR = 'SensorBus.dbc'

#Naming
SCALE_OFFSET_PREFIX = 'SCALE_OFFSET_'

# Don't change
script_dir = os.path.dirname(os.path.abspath(__file__))
SOURCE_OUT_DIR = f"{script_dir}/DBCGen/Src"
HEADER_OUT_DIR = f"{script_dir}/DBCGen/Inc"
OUT_NAME = 'dbc'