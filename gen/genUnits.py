def generateUnitCode(message):
    unitcode = ""
    for signal in message.signals:
        unitcode += f"#define {message.name.upper()}_{signal.name.upper()}_UNIT \"{signal.unit}\"\n"

    return unitcode