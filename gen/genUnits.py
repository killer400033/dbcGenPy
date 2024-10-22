def generateUnitCode(message):
    unitcode = ""
    for signal in message.signals:
        unitcode += f"#define {signal.name.upper()}_UNIT \"{signal.unit}\"\n"

    return unitcode