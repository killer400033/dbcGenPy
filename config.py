# Code generation settings
USE_SIGFLOAT = False # Sets whether the Unpack and Pack functions use a float with scaling+offset applied, or an integer with scaling+offset not applied
SIGFLOAT_TYPE = 'double'
FLOAT_LITERAL_PREC = 6 # number of decimal points in generated floating literals

# options
GENERATE_PACK = True
GENERATE_UNPACK = True
GENERATE_SIGNAL_UNITS = False
GENERATE_SIGNAL_ENUMS = True
GENERATE_SIGNAL_VALS = True
GENERATE_SIGNAL_TYPE_DECODE = True

# Locations
DBC_DIR = 'SensorBus.dbc'

# Naming
UNPACK_SCALE_OFFSET_PREFIX = 'UNPACK_SCALE_OFFSET_'
PACK_SCALE_OFFSET_PREFIX = 'PACK_SCALE_OFFSET_'

# Don't change
SOURCE_OUT_DIR = f"./DBCGen/Src"
HEADER_OUT_DIR = f"./DBCGen/Inc"
MAIN_NAME = 'dbc'
SIGNAL_VALS_NAME = 'sig_vals'
SIGNAL_UNITS_NAME = 'sig_units'
SIGNAL_ENUMS_NAME = 'sig_enum'
SIGNAL_TYPE_DECODE_NAME = 'sig_type_dec'
BYTE_INIT_VALUE = '0u'