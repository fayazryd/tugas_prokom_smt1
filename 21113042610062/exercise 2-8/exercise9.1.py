class Restaurant:
    """Model sederhana sebuah restoran."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_Restaurant(self):
        print("Nama restoran:", self.restaurant_name)
        print("Jenis makanan:", self.cuisine_type)

    def open_Restaurant(self):
        print("Restoran", self.restaurant_name, "sedang buka!")

restaurant = Restaurant('Warung Makan Bu Tini', 'Jawa')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_Restaurant()
restaurant.open_Restaurant()