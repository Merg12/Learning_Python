class Restaurant():
    """description"""

    def __init__(self, restaurant_name, cuisine_name):
        self.restaurant_name = restaurant_name
        self.cuisine_name = cuisine_name

    def describe_restaurant(self):
        print("the name of the restaurant is " + self.restaurant_name.title() + " and it serves " + self.cuisine_name.title() + " food!")

    def open_restaurant(self):
        print("we're open!")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_name = 'ice cream'):
        super().__init__(restaurant_name, cuisine_name)
        self.flavors = []
    
    def show_flavors(self):
        return self.flavors

ice_cream = IceCreamStand('martys')
ice_cream.flavors = ['cherry', 'strawbaby', 'chocowik']

ice_cream.describe_restaurant()

for flavor in ice_cream.flavors:
    print(flavor)