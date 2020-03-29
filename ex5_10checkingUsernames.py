currentUsers = ['logan', 'aliCe', 'Julie', 'hArley', 'braD']

newUsers = ['matthew', 'alice', 'Julie', 'avery', 'brad']

print(currentUsers)

for elem_currentUsers in currentUsers:
    #print(elem_currentUsers)
    newElem = elem_currentUsers.lower()
    #print("Lowered: " + newElem)
    #currentUsers.append(newElem) #adding this creates a recursion, it just keeps adding more to the list, and the for loop keeps running because every cycle adds more elements to the list
    newUsers.append(newElem)

print(newUsers)
print(newElem)

#    currentUsers.append(newElem)
#    print(currentUsers)
#for elem_newUsers in newUsers:
#    if elem_newUsers.lower() in currentUsers:
#        print("Sorry, " + elem_newUsers + " is currently in use, please enter a new username")
#    else:
#        print("User " + elem_newUsers + " is available")