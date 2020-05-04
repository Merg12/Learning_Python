file_name = 'ex10_1learning_python_text.txt'

with open(file_name) as file_object:
    lines = file_object.read()
    print("the entire file is:\n" + lines)

print(lines) #oh good, so we can use the variable we created again and again outside the open()
print(lines + " part 2")