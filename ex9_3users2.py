class User:
    def __init__(self, first_name, last_name, other_attribute):
        self.full_name = first_name.title() + " " + last_name.title()
        self.other_attribute = other_attribute

    def describe_user(self):
        print(self.full_name + " is a " + self.other_attribute.upper())

    def greet_user(self):
        print("Hello " + self.full_name)

user1 = User("larry", "smith", "monster")

user1.describe_user()
user1.greet_user()

user2 = User("greg", "gossman", "freak")

user2.describe_user()
user2.greet_user()

user3 = User("becky", "grims", "model")

user3.describe_user()
user3.greet_user()