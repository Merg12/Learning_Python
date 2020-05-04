import json

numbers = [2,3,5,7,11,13]

file_name = 'numbers.json'

with open(file_name, 'w') as file_object:
    json.dump(numbers, file_object)