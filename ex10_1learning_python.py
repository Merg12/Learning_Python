file_name = 'ex10_1learning_python_text.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()
    print(lines)

one_line = ''
for line in lines:
    one_line += line

print(one_line)