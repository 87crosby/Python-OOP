class User:
    def __init__(self,name):
        self.name = name
        self.account = BankAccount(2.5,0)
    
    def make_deposit(self, deposit):
        choice = input("Which account do you want to deposit in? Press C for checking or Press S for savings ")
        if choice.lower() == 'c':
            self.account.balance = self.account.balance + deposit
        else:
            self.account_new.balance = self.account_new.balance + deposit
        return self

    def make_withdrawal(self, withdrawal):
        choice = input("Which account do you want to withdraw from? Press C for checking or Press S for savings ")
        if choice.lower() == 'c':
            self.account.balance = self.account.balance - withdrawal
        else:
            self.account_new.balance = self.account_new.balance - withdrawal
        return self
    
    def open_account(self, name, amount):
        self.account_new = BankAccount(name,balance=amount)

    def display_balance(self):
        choice = input("Which account balance do you want to display? Press C for checking or Press S for savings ")
        if choice.lower() == 'c':
            return self.account.balance
        else: return self.account_new.balance

    def transfer(self, amount, payee):
        self.account.balance = self.account.balance - amount
        payee.account.balance = payee.account.balance + amount

class BankAccount:
    master_account_list = []
    # don't forget to add some default values for these parameters!
    def __init__(self, name = "Checking", int_rate=0, balance=0):
        self.name = name
        self.int_rate=int_rate
        self.balance=balance
        BankAccount.master_account_list.append(self)
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self

    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self

    def display_account_info(self):
        print(self.balance)
        return self.balance

    def yield_interest(self):
        self.balance = ((self.int_rate/100)*self.balance) + self.balance
        return self

    @classmethod
    def all_balances(cls):
        for i in cls.master_account_list:
            print(i.balance)

geed = User("Geed")
geed.open_account("Savings",500)
geed.make_deposit(500)
print(geed.display_balance())
#print(geed.account_new.display_account_info())