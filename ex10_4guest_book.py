file_name = 'guest_book.txt'

with open(file_name, 'a') as file_object:
    
    status = True

    while status:

        user_name = input("What's your name?")
        print("Thank you for joining us " + user_name)
        
        file_object.write(user_name + "\n")
        
        finished = input("Is there anyone else in your party? y/n")
        
        if finished == 'y':
            continue
        elif finished == 'n':
            break
        else:
            print("Invalid response, please try again")
            continue