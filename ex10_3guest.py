file_name = 'guest.txt'

user_name = input("What is your name?\n")

with open(file_name, 'a') as file_object:
    file_object.write(str(user_name) + "\n")