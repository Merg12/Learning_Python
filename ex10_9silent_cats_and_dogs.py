file_name_cats = 'cats.txt'
file_name_dogs = 'dogs.txt'

with open(file_name_cats) as file_object:
    print(file_object.read())

try:
    with open(file_name_dogs) as file_object:
        variable = file_object.read()
except FileNotFoundError:
    pass
else:
    print(variable)