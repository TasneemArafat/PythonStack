class BankAccount:
    def __init__(self, int_rate=.01, balance=0):
        self.interest = int_rate
        self.account_balance = balance
    def deposit(self, amount):
        self.account_balance += amount
    def withdraw(self, amount):
        if(amount>self.account_balance):
            print("Insufficient funds: Charging a $5 fee")
            self.account_balance -= 5
        else:
            self.account_balance -= amount
    def display_account_info(self):
        print(f"Balance: ${self.account_balance}")
    def yield_interest(self):
        if(self.account_balance>0):
            self.account_balance += (self.account_balance*self.interest)

firstaccount = BankAccount()
secondacount = BankAccount()

firstaccount.deposit(30)
firstaccount.deposit(50)
firstaccount.deposit(10)
firstaccount.withdraw(40)
firstaccount.yield_interest()
firstaccount.display_account_info()

secondacount.deposit(50)
secondacount.deposit(50)
secondacount.withdraw(10)
secondacount.withdraw(20)
secondacount.withdraw(30)
secondacount.withdraw(30)
secondacount.yield_interest()
secondacount.display_account_info()




		
