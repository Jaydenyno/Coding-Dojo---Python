class BankAccount:
    
    def __init__(self, int_rate=0, balance=0): 
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self
        
    def withdrawal(self, amount):
        if self.balance - amount < 0:
            print("Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self
        
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
     
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * (self.int_rate / 100))
        return self
    

class User:
    def __init__(self, firstName, lastName, email, age, is_reward_member = False, gold_card_point = 0):
        self.first_name = firstName
        self.last_name = lastName
        self.email = email
        self.age = age
        self.account = BankAccount(int_rate=0, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)

    def make_wwithdrawal(self, amount):
        self.account.withdrawal(amount)

    def display_user_balance(self):
        self.account.display_account_info()

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)

    def enroll(self):
        if self.is_reward_member == True:
            print("User already a member")
            return False
        else:
            return True
        # self.is_reward_member = True
        self.gold_card_point = 200

    def spend_points(self, amount):
        self.gold_card_point -= amount



user1 = User("Jayden", "No", "qwer1234@gmail.com", 23, BankAccount(int_rate=5, balance=1000))
user1.make_wwithdrawal(400)
print(user1.display_user_balance)