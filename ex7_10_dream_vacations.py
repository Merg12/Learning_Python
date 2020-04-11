user_vacation_list = {}

active = True

while active:
    user = input("what's your name?")
    vacation = input("where would you go?")

    user_vacation_list[user] = vacation

    more_users = input("anyone else? y/n")

    if more_users == 'n':
        active = False
    elif more_users == 'y':
        continue
    else:
        break

print("The results are:")
for user,vacation in user_vacation_list.items():
    print(user + " wants to go to " + vacation)