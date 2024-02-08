from itertools import permutations
def fuunc(string):
    perms = permutations(string)
    for i in perms:
        print(str(i))
