class Restaurant():
    """description"""

    def __init__(self, restaurant_name, cuisine_name):
        self.restaurant_name = restaurant_name
        self.cuisine_name = cuisine_name
        self.number_served = 0

    def describe_restaurant(self):
        print("the name of the restaurant is " + self.restaurant_name.title() + " and it serves " + self.cuisine_name.title() + " food!")

    def open_restaurant(self):
        print("we're open!")

    def set_number_served(self):
        self.number_served = 4394

    def increment_number_served(self):
        self.number_served += 100

restaurant = Restaurant("Burger Joint", "American")

print(restaurant.number_served)
restaurant.number_served = 34
print(restaurant.number_served)

restaurant.set_number_served()
print(restaurant.number_served)

restaurant.increment_number_served()
print(restaurant.number_served)

