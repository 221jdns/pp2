import re 
s = str(input())
def ex1(text):
    x = re.search("^a.*b", text)
    if x:
        return True
    else:
        return False
print(ex1(s))
