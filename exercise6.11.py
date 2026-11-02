cities = {
    "Surakarta": {
        "country": "Indonesia",
        "population": 522000,
        "fact": "Known for its traditional culture."
    },

    "Tokyo": {
        "country": "Japan",
        "population": 14000000,
        "fact": "Known for its modern technology."
    },

    "Paris": {
        "country": "France",
        "population": 2100000,
        "fact": "Known for the Eiffel Tower."
    }
}

for city, information in cities.items():
    print(f"\nCity: {city}")

    for key, value in information.items():
        print(f"{key}: {value}")