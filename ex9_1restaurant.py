class Restaurant():
    """description"""

    def __init__(self, restaurant_name, cuisine_name):
        self.restaurant_name = restaurant_name
        self.cuisine_name = cuisine_name

    def describe_restaurant(self):
        print("the name of the restaurant is " + self.restaurant_name.title() + " and it serves " + self.cuisine_name.title() + " food!")

    def open_restaurant(self):
        print("we're open!")

restaurant = Restaurant("gregs", "thai")
restaurant.describe_restaurant()
restaurant.open_restaurant()

print(restaurant.restaurant_name.title())
print(restaurant.cuisine_name.title())