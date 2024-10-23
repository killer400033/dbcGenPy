import config

def shouldUseSigFloat(signal):
    return (signal.scale != 1 or signal.offset != 0) and config.USE_SIGFLOAT