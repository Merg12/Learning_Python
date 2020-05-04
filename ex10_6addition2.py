try:
    first_number = int(input("give me a number\n"))
    second_number = int(input("another\n"))
except ValueError:
    print("sorry, at least one of these is not a number")
else:
    addition = first_number + second_number
    print(addition)