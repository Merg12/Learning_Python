rivers = {
    'nile' : 'egypt',
    'trinity' : 'dallas',
    'mississippi river' : 'mississippi',
}

for river, state in rivers.items():
    print("The " + river + " runs through " + state + ".")

for river in rivers.keys():
    print(river)

for state in rivers.values():
    print(state)