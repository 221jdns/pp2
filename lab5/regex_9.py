import re
s = input()
def rx9(text):
    x = re.sub("([a-z])([A-Z])", "\1 \2", text)
    return x 
