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