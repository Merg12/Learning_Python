favorite_places = {
    'greg' : [1, 3, 5],
    'john' : [5, 23],
    'robert' : [53, 24, 0, 7],
}

#print(favorite_places) #debugging log

for key, value in favorite_places.items():
    print(key + "'s favorite numbers are ")
    for number in value:
        #print(number) #debugging log
        print("\t" + str(number))