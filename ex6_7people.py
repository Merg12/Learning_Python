Greg = {
    'first_name' : 'greg',
    'last_name' : 'gossman',
    'age' : '40',
    'city' : 'houston',
    }

Morgan = {
    'first_name' : 'morgan',
    'last_name' : 'tran',
    'age' : '24',
    'city' : 'austin',
}

John = {
    'first_name' : 'john',
    'last_name' : 'smith',
    'age' : '54',
    'city' : 'dallas',
}

people = [Greg, Morgan, John]

for person in people:
    for key, value in person.items():
        full_name = key['first_name' + " " + 'last_name']
        print(full_name)