class BankAccount:
    def __init__(self,balance=0,int_rate=0.01):
        self.int_rate=int_rate
        self.balance=balance
        
    def deposit(self,amount):
        self.balance+=amount
        return self
    
    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient funds: Charging a $5 fee")
            self.balance-=5
            return False
        else:
            self.balance-=amount
            return True
        
    
    def display_account_info(self):
        print(f"Balance:${self.balance}")
        return self
    
    def yield_interest(self):
        if self.balance<0:
            print("no interset is added")
        else:
            self.balance*=self.int_rate
        return self

class User:
    def __init__(self,name,email,balance=0):
        self.name=name
        self.email=email
        self.account=BankAccount(balance)
        

    def make_deposit(self,amount):
        self.account.deposit(amount)

    def make_withdraw(self,amount):
        self.account.withdraw(amount)

    def display_user_balanse(self):
        print(f"User:{self.name} , Balance:{self.account.balance}")

    def transfer_money(self,another_user,amount):
        withdrawen= self.account.withdraw(amount)
        if withdrawen:  
            another_user.account.deposit(amount)


noor=User("Noor","noor@gmail.com",100)
fatema=User("fatema","fatema@gamil.com",100)
noor.make_deposit(100)
noor.transfer_money(fatema,50)
fatema.display_user_balanse()
noor.display_user_balanse()
fatema.make_withdraw(150)
fatema.display_user_balanse()
noor.account.display_account_info()