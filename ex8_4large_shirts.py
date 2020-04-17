#modify the make_shirt() function so that shirts are large by default with a message that reads
#I love python. make a large shirt and a medium shirt with the default message, and a shirt of
#any size with a different message

def make_shirt(size = 'large', message = 'I love python: '):
    print(str(message) + str(size))

make_shirt()

make_shirt("medium")

make_shirt("small", "I love sunshine: ")