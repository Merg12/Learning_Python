def build_python(first_name, last_name, age = ''):
    person = {'first' : first_name, 'last' : last_name}
    if age:
        person['age'] = age
    return person

result = build_python('bob', 'marley', '21')
print(result)