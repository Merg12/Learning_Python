from ex9_car2 import Car

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70
        self.battery = Battery()

    def describe_battery(self):
        print(str(self.battery_size))

class Battery():
    def __init__(self, battery_size = 70):
        self.battery_size = battery_size

    def describe_battery(self):
        print(str(self.battery_size))

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        print("Range is " + str(range))

    def upgrade_battery(self):
        self.battery_size = 85