import re
s = input()
def tx6(text):
    x = re.sub("\s",":",text)
    x = re.sub(",", ":", x)
    x = re.sub("[.]", ":", x)
    return x
