favorite_places = {
    "Zhafa": ["Bali", "Bandung", "Yogyakarta"],
    "Jefri Nichol": ["Jakarta", "Malang"],
    "Iqbal Ramadhan": ["Surakarta", "Bromo", "Lombok"]
}

for name, places in favorite_places.items():
    print(f"\n{name}'s favorite places:")
    for place in places:
        print(f"- {place}")