class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_description(self):
        long_name = str(self.year) + " and everything else"
        return long_name.title()

    def read_odometer(self):
        print(str(self.odometer_reading))

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("no")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery():
    def __init__(self, battery_size = 70):
        self.battery_size = battery_size

    def describe_battery(self):
        print(str(self.battery_size))

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70
        self.battery = Battery()

    def describe_battery(self):
        print(str(self.battery_size))

my_tesla = ElectricCar('honda', 'civic', '2020')
print(my_tesla.get_description())

my_tesla.describe_battery()
my_tesla.battery.describe_battery()