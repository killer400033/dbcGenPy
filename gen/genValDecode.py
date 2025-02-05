import re
from gen import helpers

def generateValDefines(message):
    code = ""
    for signal in message.signals:
        if signal.choices:
            for value, description in sorted(signal.choices.items()):
                _description = str(description)
                _description = _description.replace(' ', '_')
                _description = re.sub(r'[^a-zA-Z0-9_]', '', _description)
                code += f"#define {signal.name.upper()}__{_description.upper()} {value}\n"
    return code