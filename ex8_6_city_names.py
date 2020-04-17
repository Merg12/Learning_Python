#write a function called city_country() that takes in the name
#of a city and its country. the function should return a string
#formatted like this: "Santiago, Chile". Call your function with
#at least three city-country pairs, and print the value that's
#returned

def city_country(city_name, country_name):
    format = city_name.title() + ", " + country_name.title()
    return format

formated_name = city_country('houston', 'united states')
print(formated_name)