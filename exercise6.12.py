cities = {
    "Surakarta": {
        "country": "Indonesia",
        "population": 522000,
        "fact": "Known for its traditional culture.",
        "language": "Indonesian",
        "landmark": "Keraton Surakarta"
    },

    "Tokyo": {
        "country": "Japan",
        "population": 14000000,
        "fact": "Known for its modern technology.",
        "language": "Japanese",
        "landmark": "Tokyo Tower"
    },

    "Paris": {
        "country": "France",
        "population": 2100000,
        "fact": "Known for the Eiffel Tower.",
        "language": "French",
        "landmark": "Eiffel Tower"
    }
}

for city, information in cities.items():
    print(f"\n===== {city} =====")

    for key, value in information.items():
        print(f"{key.title()}: {value}")