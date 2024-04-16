import re
s = input() 
def rx1(text):
    x = re.search("a*b", text)
    if x:
        return True
    else:
        return False
print(rx1(s))