class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"Mobil dapat menempuh sekitar {range} mil.")

    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100


class ElectricCar:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.battery = Battery()


my_car = ElectricCar("Nissan", "Leaf", 2024)

my_car.battery.get_range()

my_car.battery.upgrade_battery()

my_car.battery.get_range()