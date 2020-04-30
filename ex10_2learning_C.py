file_name = 'ex10_1learning_python_text.txt'

with open(file_name) as file_object:
    all_text = file_object.read()

new_text = all_text.replace('Python', 'C')
print(new_text) 