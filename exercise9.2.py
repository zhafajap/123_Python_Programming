class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} menyajikan {self.cuisine_type}.")


restaurant1 = Restaurant("Restoran Padang", "Masakan Padang")
restaurant2 = Restaurant("Sushi House", "Masakan Jepang")
restaurant3 = Restaurant("Pizza Corner", "Masakan Italia")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()