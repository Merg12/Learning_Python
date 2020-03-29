ordinalList = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

#ordinalList = list(range(1, 10)) #this would make a list of int's from 1 to 9 but we would have to cast str(#) to it

for elem_List in ordinalList:
    if elem_List == '1':
        print(elem_List + 'st')
    elif elem_List == '2':
        print(elem_List + 'nd')
    elif elem_List == '3':
        print(elem_List + 'rd')
    else:
        print(elem_List + 'th')