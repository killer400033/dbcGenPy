import re

def generateEnumCode(message):
    enumcode = ""
    for signal in message.signals:
        enumcode += f"\ti{message.frame_id}_{signal.name},\n"
    return enumcode