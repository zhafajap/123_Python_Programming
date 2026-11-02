favorite_numbers = {
    "Zhafa Mortadha": [7, 10, 21],
    "Jefri Nichol": [8, 12],
    "Iqbal Ramadhan": [5, 9, 15],
    "Ari Irham": [11, 22],
    "Angga Yunanda": [3, 6, 18]
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name}'s favorite numbers:")
    for number in numbers:
        print(number)