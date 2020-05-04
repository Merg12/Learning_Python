file_name = 'responses.txt'

with open(file_name, 'a') as file_object:
    while True:
        response = input("why do you like programming?")
        file_object.write(response + "\n")
        done = input("are you done? y/n\n")

        if done == 'y':
            break
        elif done == 'n':
            continue
        else:
            print("invalid response, please try again")
            continue