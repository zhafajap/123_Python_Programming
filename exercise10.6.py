try:
    number1 = int(input("Masukkan angka pertama: "))
    number2 = int(input("Masukkan angka kedua: "))

    result = number1 + number2

    print(f"Hasil penjumlahan: {result}")

except ValueError:
    print("Input harus berupa angka.")