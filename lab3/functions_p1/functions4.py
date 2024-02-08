def isprime(n):
    if n <=1:
        return False
    if n <=3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True
def filter_prime(list):
    list_2 =[]
    n = len(list)
    for i in list:
        if isprime(i)==True:
            list_2.append(i)
    return list_2
        
        