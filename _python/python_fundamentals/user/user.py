from bank_account import BankAccount
class User:
    def __init__(self, name, email,number=1):
        self.name = name
        self.email = email
        self.accountsnumber = number
        self.bank_accounts = []
        for i in range(number):
            self.bank_accounts.append(BankAccount())
    def make_deposit(self, amount,i):
        self.bank_accounts[i-1].deposit(amount)
        return self
    def make_withdrawal(self, amount,i):
        self.bank_accounts[i-1].withdraw(amount)
        return self
    def display_user_balance(self):
        print(f"User: {self.name}")
        for i in range(len(self.bank_accounts)):
            self.bank_accounts[i].display_account_info()
        return self
    def transfer(self,other_user,amount,selfaccountnum,otheraccountnum):
        self.make_withdrawal(amount,selfaccountnum)
        other_user.make_deposit(amount,otheraccountnum)
        return self

tasneem = User("tasneem","Tasneem@gmail.com",2)
amro = User("Amro","Amro@gmail.com",1)
hadeel = User("Hadeel","Hadeel@gmail.com")

tasneem.make_deposit(100,1).make_deposit(200,2).make_deposit(300,1).make_withdrawal(200,2).display_user_balance()

amro.make_deposit(500,1).make_deposit(300,1).make_withdrawal(700,1).make_withdrawal(50,1).display_user_balance()

hadeel.make_deposit(1000,1).make_withdrawal(200,1).make_withdrawal(500,1).make_withdrawal(200,1).display_user_balance()

tasneem.transfer(hadeel,100,2,1).display_user_balance()
hadeel.display_user_balance()


    