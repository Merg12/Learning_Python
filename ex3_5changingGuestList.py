invitePeople = ["jim", "rich", "robert", "nam"]

print("come to dinner " + invitePeople[0].title() + "!")
print("come to dinner " + invitePeople[1] + "!")
print("come to dinner " + invitePeople[2] + "!")
print("come to dinner " + invitePeople[3] + "!")

noShowGuest = invitePeople.pop(2)
print("one of our guests " + noShowGuest.title() + " couldn't make it this time")
print(invitePeople)