class User:
    def __init__(self, firstName, lastName, email, age, is_reward_member = False, gold_card_point = 0):
        self.first_name = firstName
        self.last_name = lastName
        self.email = email
        self.age = age

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


user1 = User("Jayden", "No", "qwer1234@gmail.com", 23)
user2 = User("Qw", "Er" "rewq4321@gmail.com", 32)

user1.display_info()
user1.enroll()
user1.spend_points(50)

user2.display_info()
user2.enroll()
user2.spend_points(80)