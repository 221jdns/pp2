import re
s = input()
def rx7(text):
    return re.sub("_([a-z])", lambda x: x.group(1).upper(), text)
