paul = {
    'type' : 'dog',
    'owner' : 'adrian',
}

fred = {
    'type' : 'cat',
    'owner' : 'greg',
}

buster = {
    'type' : 'hamster',
    'owner' : 'phillip',
}

pets = [paul, fred, buster]
#print(pets) #debugging log

for pet in pets:
    for key, value in pet.items():
        if 'type' in key:
            print("The " + key + " of animal is a " + value)
        if 'owner' in key:
            print("\tand the owner' name is " + value)