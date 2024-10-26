import config

def shouldUseSigFloat(signal, overwrite_sigfloat=None):
    use_sigfloat = overwrite_sigfloat if overwrite_sigfloat else config.USE_SIGFLOAT
    return (signal.scale != 1 or signal.offset != 0) and use_sigfloat

def getSignalDataType(signal, overwrite_sigfloat=None):
    data_type = ""

    length = signal.length
    signed = signal.is_signed

    if shouldUseSigFloat(signal, overwrite_sigfloat):
        data_type = config.SIGFLOAT_TYPE
    else:
        if signed:
            if length <= 8:
                data_type = "int8_t"
            elif length <= 16:
                data_type = "int16_t"
            elif length <= 32:
                data_type = "int32_t"
            else:
                data_type = "int64_t"
        else:
            if length <= 8:
                data_type = "uint8_t"
            elif length <= 16:
                data_type = "uint16_t"
            elif length <= 32:
                data_type = "uint32_t"
            else:
                data_type = "uint64_t"
    return data_type