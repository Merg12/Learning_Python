list = range(1, 11)

for value in list:
    value = value**2
    print(value)


squared = [value**2 for value in range(1, 11)]
print(squared)