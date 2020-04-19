class Restaurant():
    """description"""

    def __init__(self, restaurant_name, cuisine_name):
        self.restaurant_name = restaurant_name
        self.cuisine_name = cuisine_name

    def describe_restaurant(self):
        print("the name of the restaurant is " + self.restaurant_name.title() + " and it serves " + self.cuisine_name.title() + " food!")

    def open_restaurant(self):
        print("we're open!")

instance1 = Restaurant("greg", "thai")

instance1.describe_restaurant()
instance1.open_restaurant()
print(instance1.restaurant_name)
print(instance1.cuisine_name)

instance2 = Restaurant("john", "japanese")

instance2.describe_restaurant()
instance2.open_restaurant()
print(instance2.restaurant_name)
print(instance2.cuisine_name)

instance3 = Restaurant("alice", "vietnamese")

instance3.describe_restaurant()
instance3.open_restaurant()
print(instance3.restaurant_name)
print(instance3.cuisine_name)