import re
s = input()
def rx5(text):
    x = re.findall("a.*b$",text)
    return x 

