# Code generation settings
USE_SIGFLOAT = True
SIGFLOAT_TYPE = 'double'
FLOAT_LITERAL_PREC = 6 # number of decimal points in generated floating literals

# options
GENERATE_SIGNAL_UNITS = False
GENERATE_SIGNAL_ENUMS = False
GENERATE_SIGNAL_VALS = False

# Locations
DBC_DIR = 'SensorBus.dbc'

#Naming
SCALE_OFFSET_PREFIX = 'SCALE_OFFSET_'

# Don't change
SOURCE_OUT_DIR = f"../DBCGen/Src"
HEADER_OUT_DIR = f"../DBCGen/Inc"
MAIN_NAME = 'dbc'
SIGNAL_VALS_NAME = 'sig_vals'
SIGNAL_UNITS_NAME = 'sig_units'
SIGNAL_ENUMS_NAME = 'sig_enum'