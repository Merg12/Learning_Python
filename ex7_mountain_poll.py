responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name?")
    response = input("Which mountain would you like to climb someday?")

    responses[name] = response #store response in dictionary responses

    repeat = input("Anyone else? y/n")
    if repeat == 'n':
        polling_active = False

for name,response in responses.items():
    print(name + " would like to climb " + response)