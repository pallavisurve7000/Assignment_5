# Handleing a bank account

class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    
    def withdrawal(self, amount):
        self.balance-= amount

    def deposit(self, amount):
        self.balance+= amount

    def getBalance(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
            super().__init__(title, balance)
            self.interestRate = interestRate
    
    def interestAmount(self):
        self.intamount = (self.interestRate * self.balance)/100
        return self.intamount
    
    def get_Details(self):
         print(f"\nName :{self.title}\nBalance :{self.balance}\nInterest Rate :{self.interestRate}\n")

acc = SavingsAccount()
while True:
    options = int(input("\n1)set details\n2)deposit\n3)withdraw\n4)interest amount\n5)view details\n6exit\n"))
    if options == 1:
        name = input("Enter name :")
        balance = int(input("Enter balance :"))
        intrate = int(input("Enter intrest rate :"))
        acc.__init__(name,balance,intrate)
    elif options == 2:
        amount = int(input("Enter amount to deposit :"))
        acc.deposit(amount)
    elif options == 3:
        amount = int(input("Enter amount to withdraw :"))
        acc.withdrawal(amount)
    elif options == 4:
        amt = acc.interestAmount()
        print(f"\nIntrest Amount : {amt}\n")
    elif options == 5:
        acc.get_Details()
    else:
        exit(1)