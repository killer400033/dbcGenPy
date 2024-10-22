# Code generation settings
USE_SIGFLOAT = True
SIGFLOAT_TYPE = 'double'
FLOAT_LITERAL_PREC = 6 # number of decimal points in generated floating literals

# options
GENERATE_UNITS = True
GENERATE_ENUMS = True

# Locations
DBC_DIR = 'SensorBus.dbc'
SOURCE_OUT_DIR = 'generated'
HEADER_OUT_DIR = 'generated'

OUT_NAME = 'dbc'

#Naming
SCALE_OFFSET_PREFIX = 'SCALE_OFFSET_'