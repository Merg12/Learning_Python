#start with a copy of your program from 8_9. wright a function called
#make_great() that modifies the list of magicians by adding the
#phrase the great to each magician's name. call show_magicians() to
#see the list that the list has actually been modified

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

make_great(magician_list)
show_magicians(new_list)