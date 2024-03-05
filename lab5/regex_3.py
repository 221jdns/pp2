import re 
s = input()
def rx3(text):
    x = re.findall("[a-z]_[a-z]", text)
    if x:
        return True
    else:
        return False 
print(rx3(s))