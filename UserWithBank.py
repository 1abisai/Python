class BankAccount:
    def __init__(self, account, int_rate=0.2, balance=0): 
        self.account = account
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount, account):
        self.balance = self.balance + amount
        return self
    
    def withdraw(self, amount, account):
        if(self.balance < amount):
            print("Insufficient balance!")
        else: 
            self.balance = self.balance - amount
        return self
    
    def display_account_info(self):
        print('Balance:', account.balance)
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.int_rate)
        return self

class User: 
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(account=" ", int_rate=0.2, balance=0)
    
    def make_deposit(self, amount, account):
        self.account.deposit(amount, account)
        return self

    def make_withdrawal(self, amount, account):
        self.account.withdraw(amount, account)
        return self

    def display_user_balance(self):
        self.account.display_account_info()
        return self

Dan = User("Daniel", "dan@email.com")

checking = BankAccount('checking',0.2)

Dan.make_deposit(200,checking).make_withdrawal(100,checking)