import re
s = input()
def rx10(text):
    return re.sub("[a-z][A-Z]", lambda x: x.group(1) + '_'x.group(1),lower(),text)