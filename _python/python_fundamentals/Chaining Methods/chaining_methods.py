class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):	
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        if(self.account_balance == 0 or amount>=self.account_balance):
            print("Not enought money")
            return self
        else:
            self.account_balance -= amount
            return self
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self
    def transfer(self,other_user,amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self

tasneem = User("tasneem","Tasneem@gmail.com")
amro = User("Amro","Amro@gmail.com")
hadeel = User("Hadeel","Hadeel@gmail.com")


tasneem.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(200).display_user_balance()

amro.make_deposit(500).make_deposit(300).make_withdrawal(700).make_withdrawal(50).display_user_balance()

hadeel.make_deposit(1000).make_withdrawal(200).make_withdrawal(500).make_withdrawal(200).display_user_balance()

tasneem.transfer(hadeel,100).display_user_balance()
hadeel.display_user_balance()