currentUsers = ['logan', 'alice', 'julie', 'harley', 'brad']

newUsers = ['matthew', 'alice', 'julie', 'avery', 'brad']

for elem_newUsers in newUsers:
    if elem_newUsers in currentUsers:
        print("Sorry, " + elem_newUsers + " is currently in use")
    else:
        print("User " + elem_newUsers + " is good to go")