import re
s = input() 
def rx2(text):
    x = re.search("a{2,3}b", text)
    if x:
        return True
    else:
        return False
print(rx2(s))
