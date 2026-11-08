class User:
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city

    def describe_user(self):
        print(f"Nama: {self.first_name} {self.last_name}")
        print(f"Umur: {self.age}")
        print(f"Kota: {self.city}")

    def greet_user(self):
        print(f"Halo, {self.first_name}! Selamat datang.")


user1 = User("Andi", "Saputra", 20, "Surakarta")
user2 = User("Budi", "Santoso", 21, "Yogyakarta")
user3 = User("Citra", "Putri", 19, "Semarang")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()