class BankAccount:
    master_account_list = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate=0, balance=0):
        self.int_rate=int_rate
        self.balance=balance
        BankAccount.master_account_list.append(self)
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self
    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self
    def display_account_info(self):
        print(self.balance)
        return self
    def yield_interest(self):
        self.balance = ((self.int_rate/100)*self.balance) + self.balance
        return self
    @classmethod
    def all_balances(cls):
        for i in cls.master_account_list:
            print(i.balance)

dankus = BankAccount(1.5,1000)
memecus = BankAccount(1,1000)

dankus.deposit(500).deposit(200).deposit(800).withdraw(500).yield_interest().display_account_info()
memecus.deposit(1000).deposit(1000).withdraw(500).withdraw(500).withdraw(500).withdraw(500).yield_interest().display_account_info()

BankAccount.all_balances()