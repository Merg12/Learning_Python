def build_person(first_name, last_name):
    full_name = {'first' : first_name, 'last' : last_name}
    return full_name

result = build_person('bob', 'ross')
print(result)