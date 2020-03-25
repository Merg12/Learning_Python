listOfNames = ['admin', 'john', 'logan', 'alice', 'julie']

if listOfNames:
    for elem_listOfNames in listOfNames:
        if elem_listOfNames == 'admin':
            print("Hello " + elem_listOfNames + ", would you like to see a status report?")
        else:
            print("Hello " + elem_listOfNames + ", it is good to see you again.")
else:
    print("We need to find some users!")