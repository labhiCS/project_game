class User():
    def __init__(self, first_name, last_name, age, profession):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age 
        self.profession = profession.title()
    
    def describe_user(self):
        print(self.first_name + " " + self.last_name + " is a " + self.profession)

user = User('abhi', 'lamichhane', 15, 'student')
user1 = User('anup', 'thapa', 22, 'business man')

user.describe_user()
user1.describe_user()