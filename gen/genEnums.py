import re

def generateEnumCode(message):
    enumcode = ""
    for signal in message.signals:
        if signal.choices:
            enumcode += f"// Value table for {signal.name}\n"
            enumcode += f"enum {signal.name.upper()}_VAL {{\n"
            for value, description in signal.choices.items():
                description = str(description)
                description = description.replace(' ', '_')
                description = re.sub(r'[^a-zA-Z0-9_]', '', description)

                enumcode += f"\t_{description.upper()} = {value},\n"
            enumcode += "};\n\n"

    return enumcode