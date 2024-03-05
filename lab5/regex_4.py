import re 
s = input()

def rx4(text):
    x = re.findall("[A-Z][a-z]",text)
    return x 

