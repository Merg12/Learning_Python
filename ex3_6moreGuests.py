invitePeople = ["jim", "rich", "robert", "nam"]

print("come to dinner " + invitePeople[0].title() + "!")
print("come to dinner " + invitePeople[1] + "!")
print("come to dinner " + invitePeople[2] + "!")
print("come to dinner " + invitePeople[3] + "!")

noShowGuest = invitePeople.pop(2)
print("one of our guests " + noShowGuest.title() + " couldn't make it this time")
print(invitePeople)

addGuestToBeginning = invitePeople.insert(0,"bob")
addAnotherGuestToMiddle = invitePeople.insert(3, "steve")
invitePeople.append("greg")

print("we found a bigger table!")
print(invitePeople)

print("oops sorry, our table can only fit 2 people now")

removedGuest = invitePeople.pop()
print("we are very sorry " + removedGuest.title() + " bye-bye")
removedGuest = invitePeople.pop()
print("we are very sorry " + removedGuest.title() + " bye-bye")
removedGuest = invitePeople.pop()
print("we are very sorry " + removedGuest.title() + " bye-bye")

del invitePeople[0]
print(invitePeople)

del invitePeople[0]
print(invitePeople)

del invitePeople[0]
print(invitePeople)