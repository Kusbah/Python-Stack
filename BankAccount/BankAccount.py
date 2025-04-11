class BankAccount:
    def __init__(self,balance =0 , int_rate = 0.01):
        self.balance = balance
        self.int_rate = int_rate
 
    def deposit(self, amount):
        self.balance += amount
       
    def withdraw(self, amount):
        self.balance -= amount
 
    def display_account_info(self):
        print(f"current balance is {self.balance}")
 
    def yield_interest(self):
        self.balance += self.balance * self.int_rate
 
karam = BankAccount(200)
Abdallah = BankAccount(150)
karam.deposit(50)
karam.deposit(50)
karam.deposit(50)
karam.withdraw(100)
karam.yield_interest()
karam.display_account_info()

Abdallah.deposit(200)
Abdallah.deposit(120)
Abdallah.withdraw(50)
Abdallah.withdraw(100)
Abdallah.withdraw(100)
Abdallah.withdraw(100)
Abdallah.yield_interest()
Abdallah.display_account_info()
