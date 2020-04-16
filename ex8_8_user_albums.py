#start with your program from 8_7. write a while loop that allows users
#to enter an album's artist and titel. once you have that info, call
#make_album() with the user's input and print the dictionary that's
#created. Be sure to include a quit value in the while loop

def make_album():

    artist_album = {}

    while True:
        input_artist = input("whats the artists name: \nenter 'q' to quit\n")
        if input_artist == 'q':
            break

        input_album = input("whats the albums title: \nenter 'q' to quit\n")
        if input_album == 'q':
            break

        artist_album[input_artist] = input_album


    return artist_album

print(make_album())