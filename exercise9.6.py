class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} menyajikan masakan {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} sedang buka!")


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type='es krim'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        print(f"Rasa es krim di {self.restaurant_name}:")
        for flavor in self.flavors:
            print(f"- {flavor}")


stand = IceCreamStand('Es Krim Tip Top')
stand.flavors = ['vanila', 'cokelat', 'stroberi', 'durian']
stand.describe_restaurant()
stand.show_flavors()
