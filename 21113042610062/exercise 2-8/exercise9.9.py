class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def get_range(self):
        if self.battery_size == 40:
            jarak = 150
        elif self.battery_size == 65:
            jarak = 225
        else:
            jarak = 0

        print("Jarak tempuh:", jarak, "mil")

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65


class ElectricCar:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.battery = Battery()

    def describe_car(self):
        print(self.year, self.make, self.model)


mobil = ElectricCar("Nissan", "Leaf", 2024)

mobil.describe_car()

mobil.battery.get_range()

mobil.battery.upgrade_battery()

mobil.battery.get_range()