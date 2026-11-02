rivers = {
    "Nile": "Egypt",
    "Amazon": "Brazil",
    "Citarum": "Indonesia"
}

for river, country in rivers.items():
    print(f"The {river} runs through {country}.")

print("\nThe following rivers are included:")
for river in rivers.keys():
    print(river)

print("\nThe following countries are included:")
for country in rivers.values():
    print(country)