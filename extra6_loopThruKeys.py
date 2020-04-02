favoriteLanguage = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python'
}

friends = ['phil', 'sarah']

for name in favoriteLanguage.keys():
    print(name.title())

    if name in friends:
        print("Hi " + name.title() + ", your fav language is " + 
        favoriteLanguage[name].title() + "!")