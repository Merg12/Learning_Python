class User:
    def __init__(self, first_name, last_name, other_attribute):
        self.first_name = first_name
        self.last_name = last_name
        self.other_attribute = other_attribute

    def describe_user(self):
        print(self.first_name.title() + " " + self.last_name.title() + " is a " + self.other_attribute.upper())

    def greet_user(self):
        print("Hello " + self.first_name.title() + " " + self.last_name.title())

user1 = User("larry", "smith", "monster")

user1.describe_user()
user1.greet_user()

user2 = User("greg", "gossman", "freak")

user2.describe_user()
user2.greet_user()

user3 = User("becky", "grims", "model")

user3.describe_user()
user3.greet_user()