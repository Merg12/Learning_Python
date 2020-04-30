file_name = 'ex10_1learning_python_text.txt'

with open(file_name) as file_object:
    lines = file_object.read()
    print("\nThe entire file is:\n" + lines)
    print("")

with open(file_name) as file_object:
    lines2 = file_object.readlines()
print("Using the stored list:")
for line in lines2:
    print(line.strip())
print("")

with open(file_name) as file_object:
    print("Using for loop:")
    for line in file_object:
        print(line.strip())