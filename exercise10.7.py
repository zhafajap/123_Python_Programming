while True:
    try:
        number1 = input("Masukkan angka pertama (q untuk keluar): ")

        if number1.lower() == "q":
            break

        number2 = input("Masukkan angka kedua (q untuk keluar): ")

        if number2.lower() == "q":
            break

        result = int(number1) + int(number2)

        print(f"Hasil: {result}")

    except ValueError:
        print("Input tidak valid. Masukkan angka.")