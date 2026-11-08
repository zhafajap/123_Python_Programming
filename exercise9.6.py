class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        print("Pilihan rasa es krim:")
        for flavor in self.flavors:
            print(f"- {flavor}")


ice_cream = IceCreamStand(
    "Ice Cream House",
    "Dessert",
    ["Vanilla", "Chocolate", "Strawberry"]
)

ice_cream.display_flavors()