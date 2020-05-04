first_number = input("please enter the first number\n")
second_number = input("now the second number\n")

try:
    addition = int(first_number) + int(second_number)
except ValueError:
    print("wrong, need numbers!")
else:
    print(addition)