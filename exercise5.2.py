# 1. Equality dan inequality pada string
car = "subaru"

print(car == "subaru")  # True
print(car == "audi")    # False

print(car != "audi")    # True
print(car != "subaru")  # False


# 2. Menggunakan lower()
name = "Messi"

print(name.lower() == "messi")  # True
print(name.lower() == "ronaldo")  # False


# 3. Numerical tests
age = 20

print(age == 20)  # True
print(age == 18)  # False

print(age != 18)  # True
print(age != 20)  # False

print(age > 18)   # True
print(age > 25)   # False

print(age < 25)   # True
print(age < 18)   # False

print(age >= 20)  # True
print(age >= 25)  # False

print(age <= 20)  # True
print(age <= 18)  # False


# 4. Menggunakan and dan or
age = 20

print(age > 18 and age < 25)  # True
print(age > 25 and age < 30)  # False

print(age > 18 or age < 10)   # True
print(age > 25 or age < 10)   # False


# 5. Menggunakan in
players = ["Messi", "Pedri", "Yamal"]

print("Messi" in players)    # True
print("Ronaldo" in players)  # False


# 6. Menggunakan not in
print("Ronaldo" not in players)  # True
print("Messi" not in players)   # False