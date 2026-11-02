pet_1 = {
    "animal": "Cat",
    "owner": "Zhafa"
}

pet_2 = {
    "animal": "Dog",
    "owner": "Ronaldo"
}

pet_3 = {
    "animal": "Rabbit",
    "owner": "Kimi Antonelli"
}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print("\nPet Information:")
    for key, value in pet.items():
        print(f"{key}: {value}")