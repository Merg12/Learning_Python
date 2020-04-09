responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name?")
    response = input("Which mountain would you like to climb someday?")

    responses[name] = response #store response in dictionary responses

    print(responses)