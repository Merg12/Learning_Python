class User:
    def __init__(self, first_name, last_name, other_attribute):
        self.first_name = first_name
        self.last_name = last_name
        self.other_attribute = other_attribute
        self.login_attempts = 0

    def describe_user(self):
        print(self.first_name.title() + " " + self.last_name.title() + " is a " + self.other_attribute.upper())

    def greet_user(self):
        print("Hello " + self.first_name.title() + " " + self.last_name.title())

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
    
instance = User("bob", "sagat", "beast")

instance.increment_login_attempts()
print(instance.login_attempts)

instance.increment_login_attempts()
print(instance.login_attempts)

instance.increment_login_attempts()
print(instance.login_attempts)

instance.reset_login_attempts()
print(instance.login_attempts)
