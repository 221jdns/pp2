class LAB:
    s = ''
    def get_string(self):
        s = input()
    def print_string(self):
        print(s)
a = LAB()
a.get_string()




class Shape:
    def area(self):
        print(0)

class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        print(self.length**2)







class Rectangle(Shape):
    def __init__(self,width,length):
        self.width = width
        self.length = length
    def ar(self):
        print(self.length*self.width)



import math
class Point:
    def __init__(self,x,y):
        x.self = x
        y.self = y
    def show(self):
        print(x.self,y.self)
    def move(self,mx,my):
        self.x +=mx
        self.y +=my
    def dist(self, somepoint):
        distance = math.sqrt((self.x - somepoint.x)**2 +(self.y - somepoint.y)**2)
        return distance



class bank_account:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance 
    def deposit(self,amount):
        self.balance+=self.amount
    def withdraw(self,amount):
        if 0<self.amount and self.amount <=self.balance:
            self.balance -=self.amount
    return balance


class Account:pass
def isprime(n):
    if n<=1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


    









