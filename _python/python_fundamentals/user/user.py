class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    	self.account_balance += amount	# the specific user's account increases by the amount of the value received
    def make_withdrawal(self, amount):
        if(self.account_balance == 0 or amount>=self.account_balance):
            print("Not enought money")
        else:
            self.account_balance -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
    def transfer(self,other_user,amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)

tasneem = User("tasneem","Tasneem@gmail.com")
amro = User("Amro","Amro@gmail.com")
hadeel = User("Hadeel","Hadeel@gmail.com")

tasneem.make_deposit(100)
tasneem.make_deposit(200)
tasneem.make_deposit(300)
tasneem.make_withdrawal(200)
tasneem.display_user_balance()

amro.make_deposit(500)
amro.make_deposit(300)
amro.make_withdrawal(700)
amro.make_withdrawal(50)
amro.display_user_balance()

hadeel.make_deposit(1000)
hadeel.make_withdrawal(200)
hadeel.make_withdrawal(500)
hadeel.make_withdrawal(200)
hadeel.display_user_balance()

tasneem.transfer(hadeel,100)
tasneem.display_user_balance()
hadeel.display_user_balance()


    