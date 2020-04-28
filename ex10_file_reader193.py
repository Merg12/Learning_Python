filename = '/home/heroinamagazine/Visual_Studio_Code/Learning_Python/ex10_pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())