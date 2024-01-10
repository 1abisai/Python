class BankAccount():
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self
    
    def withdraw(self, amount):
        if(self.balance < amount):
            print("Insufficient balance!")
        else: 
            self.balance = self.balance - amount
        return self
    
    def display_account_info(self):
        print('Balance:', self.balance)
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.int_rate)
        return self
# first acc
acc_user = BankAccount(0.02, 50)
acc2 = BankAccount(0.08, 20)

acc_user.deposit(500)

acc_user.deposit(100)

acc_user.deposit(100)

acc_user.withdraw(300)

acc_user.withdraw(200)

acc_user.display_account_info()

acc_user.yield_interest()

acc2.yield_interest()

# acc_user.display_account_info()
# second acc

acc2.deposit(700)

acc2.deposit(200)

acc2.withdraw(300)

acc2.withdraw(100)

acc2.withdraw(200)

acc2.display_account_info()

acc2.display_account_info(), acc_user.display_account_info()