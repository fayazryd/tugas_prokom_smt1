class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_Restaurant(self):
        print("Nama restoran:", self.restaurant_name)
        print("Jenis makanan:", self.cuisine_type)

restaurant_1 = Restaurant('Warung Makan Bu Tini', 'Jawa')
restaurant_2 = Restaurant('Sushi Tei', 'Jepang')
restaurant_3 = Restaurant('Pizza Hut', 'Italia')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()