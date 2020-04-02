favoriteLanguages = {
    'trevor' : 'python',
    'logan' : 'c',
    'lin' : 'ruby',
    'morgan' : 'c++',
    'alice' : 'swift',
}

neededPeopleOnFavLanguages = ['trevor', 'greg', 'rob', 'alice']

for name in neededPeopleOnFavLanguages:
    if name not in favoriteLanguages:
        print("Hi " + name.title() + " please sign up!")
    else:
        print("Thanks for being a member " + name.title() + "!")