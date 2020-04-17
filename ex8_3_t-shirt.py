#Write a function called make_shirt() that accepts a size and the text of a message that
#should be printed on the shirt. the function should print a sentence summarizing the size
#of the shirt and the message printed on it. Call the function once using positional argument
#to make a shirt. call the function a second time using keyword arguments

def make_shirt(size, message):
    print(str(message) + str(size))

make_shirt(5, "Hi, this shirt is size: ")