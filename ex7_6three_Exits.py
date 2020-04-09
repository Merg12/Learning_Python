message_to_customers = "\nHow old are you?"
message_to_customers += "\nWhen you're done, enter 'quit'\n"

message = True

response = input(message_to_customers)

while(message == True):
    if(response == 'quit'):
        message = False
        #break
    elif(int(response) < 3):
        print("It will be FREE!")
        response = input(message_to_customers)
    elif(int(response) <= 12):
        print("It will be $10")
        response = input(message_to_customers)
    else:
        print("It will be $15")
        response = input(message_to_customers)