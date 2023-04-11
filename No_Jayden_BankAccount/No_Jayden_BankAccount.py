class BankAccount:

    # don't forget to add some default values for these parameters!
    
    def __init__(self, int_rate=0, balance=0): 
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.int_rate = int_rate
        self.balance = balance
    
    
    def deposit(self, amount):
        # your code here
        self.balance += amount
        return self
    
    
    def withdraw(self, amount):
        # your code here
        if self.balance - amount < 0:
            print("Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self
    
    
    def display_account_info(self):
        # your code here
        print(f"Balance: {self.balance}")
        return self
   
   
    def yield_interest(self):
        # your code here
        if self.balance > 0:
            self.balance += (self.balance * (self.int_rate / 100))
        return self

bankAccount1 = BankAccount(5, 1000)
bankAccount1.deposit(50).deposit(50).deposit(50).withdraw(200).yield_interest().display_account_info()


bankAccount2 = BankAccount(5, 2000)

