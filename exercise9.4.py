class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} menyajikan masakan {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} sedang buka!")

    def set_number_served(self, number):
        """Atur jumlah pelanggan yang sudah dilayani."""
        self.number_served = number

    def increment_number_served(self, increment):
        """Tambah jumlah pelanggan yang sudah dilayani."""
        self.number_served += increment


restaurant = Restaurant('Warung Makan Bu Tini', 'Jawa')
print(f"Pelanggan dilayani: {restaurant.number_served}")

restaurant.number_served = 12
print(f"Pelanggan dilayani: {restaurant.number_served}")

restaurant.set_number_served(40)
print(f"Pelanggan dilayani: {restaurant.number_served}")

restaurant.increment_number_served(25)
print(f"Pelanggan dilayani: {restaurant.number_served}")