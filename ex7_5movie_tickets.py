message_to_customers = "\nHow old are you?"
message_to_customers += "\nWhen you're done, enter 'quit'\n"

message = input(message_to_customers)

while(message != 'quit'):
    if(int(message) < 3):
        print("It will be FREE!")
        message = input(message_to_customers)
    elif(int(message) <= 12):
        print("It will be $10")
        message = input(message_to_customers)
    else:
        print("It will be $15")
        message = input(message_to_customers)