from functools import reduce
from operator import mul
import time
import math


# 1
def multiply_list(n):
    return reduce(mul, n)


n = [1, 2, 3, 4, 5]
print(multiply_list(n))


# 2
def count_case(s):
    up = sum(1 for char in s if char.isupper())
    low = sum(1 for char in s if char.islower())
    return up, low


s = "Hello World!"
up, low = count_case(s)
print(f"Upper case letters: {up}, Lower case letters: {low}")


# 3
def is_palindrome(s):
    return s == "".join(reversed(s))


print(is_palindrome("madam"))
print(is_palindrome("hello"))


# 4
def delayed_sqrt(n, delay_ms):
    time.sleep(delay_ms / 1000)
    return math.sqrt(n)


n = 25100
delay_ms = 2123
result = delayed_sqrt(n, delay_ms)
print(f"Square root of {n} after {delay_ms} milliseconds is {result}")


# 5
def arat(elements):
    return all(elements)


print(arat((True, True, True)))
print(arat((True, False, True)))