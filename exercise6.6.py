favorite_languages = {
    "Zhafa": "Python",
    "Messi": "Java",
    "Eunsoo": "Python",
    "Yamal": "C++"
}

people = ["Zhafa", "Eunsoo", "Pedri", "Yamal", "Messi"]

for person in people:
    if person in favorite_languages:
        print(f"Thank you, {person}, for responding.")
    else:
        print(f"{person}, please take our poll!")