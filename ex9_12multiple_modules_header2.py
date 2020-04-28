from ex9_12multiple_modules_header import User

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