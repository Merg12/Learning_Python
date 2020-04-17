#start with your work from 8_10. call the function make_great() with
#a copy of the list of magicians' names. because the original list
#will be changed, return the new list and store it in a separate list.
#call show_magicians() with each list to show that you have one list of
#the original names and one list with the Great added to each magician's
#name

magician_list = ['hudini', 'amazo', 'starman']
new_list = []

def make_great(names):
    while names:
        current_name = names.pop() + " the Great!"
        new_list.append(current_name)
    return new_list
    
def show_magicians(names):
    for name in names:
        print(name)

make_great(magician_list[:])
show_magicians(new_list)

show_magicians(magician_list)