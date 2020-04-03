cities = {
    'houston' : {'country' : 'US', 'population' : '4', 'fact' : 'diverse'},
    'dallas' : {'country' : 'netherland', 'population' : '1', 'fact' : 'boring'},
    'austin' : {'country' : 'austrailia', 'popuation' : '1000', 'fact' : 'fun'},
}

for key, value in cities.items():
    print("\n" + key.title() + ":")
    for innerkey, innervalue in value.items():
        print("\t" + innerkey.title() + ": " + innervalue.title())