message_to_customer = "What topping would you like?\n"
message_to_customer += "Please enter 'quit' when you are done.\n"

message = input(message_to_customer)

while(message != 'quit'):
    if(message == 'quit'):
        print("Thank you! We will work on this right away!")
        break
    else:
        print("\t" + message + " added!")
        message = input(message_to_customer)