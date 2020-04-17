#write a funciton called describe_city() that accepts the name of a city and its country. the function
#should print a simple sentence, such as Reykjavik is in Iceland. give the parameter for the country a 
#a default value. call your function for 3 different cities, at least one of which is not in the default
#country

def describe_city(city, country = 'USA'):
    print(city + " is in " + country)

describe_city("houston")
describe_city("dallas")
describe_city("sydney", "australia")