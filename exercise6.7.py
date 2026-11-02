person_1 = {
    "first_name": "Zhafa",
    "last_name": "Mohtar",
    "age": 18,
    "city": "Surakarta"
}

person_2 = {
    "first_name": "Lionel",
    "last_name": "Messi",
    "age": 39,
    "city": "Rosario"
}

person_3 = {
    "first_name": "Pedri",
    "last_name": "Gonzalez",
    "age": 21,
    "city": "Barcelona"
}

people = [person_1, person_2, person_3]

for person in people:
    print("\nPerson Information:")
    for key, value in person.items():
        print(f"{key}: {value}")