import re
from gen import helpers

def generateValDecodeFunctions(message):
    valcode = ""
    for signal in message.signals:
        if signal.choices:
            data_type = helpers.getSignalDataType(signal)
            valcode += f"// Function for getting val from {signal.name} signal\n"
            valcode += f"void Get_{signal.name}_Val({data_type} signal, char* output, uint8_t len) {{\n"
            valcode += "\tswitch(signal) {\n"
            for value, description in sorted(signal.choices.items()):
                valcode += f"\t\tcase({value}):\n"
                valcode += f"\t\t\tstrncpy(output, \"{description}\", len);\n"
                valcode += f"\t\t\tbreak;\n"
            valcode += "\t\tdefault:\n"
            valcode += "\t\t\tstrncpy(output, \"ERROR\", len);\n"
            valcode += "\t\t\tbreak;\n"
            valcode += "\t}\n"
            valcode += "}\n\n"

    return valcode

def generateValDecodeFuncPrototypes(message):
    valcode = ""
    for signal in message.signals:
        if signal.choices:
            data_type = helpers.getSignalDataType(signal)
            valcode += f"void Get_{signal.name}_Val({data_type} signal, char* output, uint8_t len);\n"
    return valcode

def generateValDefines(message):
    code = ""
    for signal in message.signals:
        if signal.choices:
            for value, description in sorted(signal.choices.items()):
                _description = str(description)
                _description = _description.replace(' ', '_')
                _description = re.sub(r'[^a-zA-Z0-9_]', '', _description)
                code += f"#define {signal.name.upper()}__{_description.upper()} \"{description}\"\n"
    return code