class User:
    def __init__(self, first_name, last_name, other_attribute):
        self.first_name = first_name
        self.last_name = last_name
        self.other_attribute = other_attribute

    def describe_user(self):
        print(self.first_name.title() + " " + self.last_name.title() + " is a " + self.other_attribute.upper())

    def greet_user(self):
        print("Hello " + self.first_name.title() + " " + self.last_name.title())

class Privileges():
    def __init__(self, privileges = ['happy', 'birthday']):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)

class Admin(User):
    def __init__(self, first_name, last_name, other_attribute = ''):
        super().__init__(first_name, last_name, other_attribute)
        self.privilege = Privileges()