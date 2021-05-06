class BankAccount:
    def __init__(self, int_rate=.01, balance=0):
        self.interest = int_rate
        self.account_balance = balance
        
    def deposit(self, amount):
        self.account_balance += amount
        return self
    def withdraw(self, amount):
        if(amount>self.account_balance):
            print("Insufficient funds: Charging a $5 fee")
            self.account_balance -= 5
            return self
        else:
            self.account_balance -= amount
            return self
    def display_account_info(self):
        print(f"Balance: ${self.account_balance}")
        return self
    def yield_interest(self):
        if(self.account_balance>0):
            self.account_balance += (self.account_balance*self.interest)
            return self

# firstaccount = BankAccount()
# secondacount = BankAccount()

# firstaccount.deposit(30).deposit(50).deposit(10).withdraw(40).yield_interest().display_account_info()

# secondacount.deposit(50).deposit(50).withdraw(10).withdraw(20).withdraw(30).withdraw(30).yield_interest().display_account_info()




		
