#make a list of magician's names. pass the list to a function called
#show_magicians(), which print the name of each magician in the list

magician_list = ['hudini', 'amazo', 'starman']

def show_magicians(names):
    for name in names:
        print(name)

show_magicians(magician_list)