#write a function that accepts a list of items a person wants on a sandwich
#the function should have 1 parameter that collects as many items as the
#function call provides, and it should print a summary of the sandwich
#that is being ordered. Call the function 3 times using a different number
#arguments each time

def sandwich_ingredients(*ingredients):
    print(ingredients)

sandwich_ingredients('ham')
sandwich_ingredients('ham', 'cheese')
sandwich_ingredients('metal', 'blades', 'knives')