class User:
    def __init__(self, name, email,balance=0):
        self.name = name
        self.email = email
        self.balance = balance
    def make_deposit(self, amount): 
        self.balance += amount
    def make_withdrawal(self, amount):
        self.balance -= amount
    def display_user_balance(self):
        print(f"Name: {self.name}\n Balance: {self.balance}")
    def transfer_money(self, other_user, amount):
        self.balance -= amount
        other_user.balance += amount

user1 = User("abd","abd@gmial.com")
user2 = User("khaild","khaild@gmial.com")
user3 = User("ahmad","ahmad@gmial.com")

user1.make_deposit(100)
user1.make_deposit(100)
user1.make_deposit(100)
user1.make_withdrawal(100)
user1.display_user_balance()

user2.make_deposit(200)
user2.make_deposit(100)
user2.make_withdrawal(100)
user2.make_withdrawal(100)
user2.display_user_balance()

user1.transfer_money(user2,50)
user1.display_user_balance()
user2.display_user_balance()