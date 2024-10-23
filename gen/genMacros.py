import config
from gen import helpers

# Given a can signal, generates the macros for offset and scaling
def generateMacros(message):
    macroCode = ""
    for signal in message.signals:
        if helpers.shouldUseSigFloat(signal):
            macroCode += f"#define {config.SCALE_OFFSET_PREFIX}{signal.name.upper()}(x) "
            precision = config.FLOAT_LITERAL_PREC
            macroCode += f"( (((x) * ({float(signal.scale):.{precision}f})) + ({float(signal.offset):.{precision}f})) );\n"
            
    return macroCode