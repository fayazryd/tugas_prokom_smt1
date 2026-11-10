class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Nama restoran:", self.restaurant_name)
        print("Jenis makanan:", self.cuisine_type)


restaurant1 = Restaurant("Warung Padang", "Masakan Padang")
restaurant2 = Restaurant("Kedai Jepang", "Makanan Jepang")
restaurant3 = Restaurant("Restoran Italia", "Masakan Italia")

restaurant1.describe_restaurant()
print()

restaurant2.describe_restaurant()
print()

restaurant3.describe_restaurant()