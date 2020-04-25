class User:
    def __init__(self, first_name, last_name, other_attribute):
        self.first_name = first_name
        self.last_name = last_name
        self.other_attribute = other_attribute

    def describe_user(self):
        print(self.first_name.title() + " " + self.last_name.title() + " is a " + self.other_attribute.upper())

    def greet_user(self):
        print("Hello " + self.first_name.title() + " " + self.last_name.title())

class Admin(User):
    def __init__(self, first_name, last_name, other_attribute = ''):
        super().__init__(first_name, last_name, other_attribute)
        self.privileges = []

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)

instance = Admin('greg', 'gossman')

instance.privileges = ["can add post", "can delete posts", "can ban user"]

instance.show_privileges()

