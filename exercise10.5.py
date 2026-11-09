from pathlib import Path

path = Path("guest_book.txt")

while True:
    name = input("Masukkan nama (ketik 'q' untuk berhenti): ")

    if name.lower() == "q":
        break

    print(f"Halo, {name}! Selamat datang.")

    with path.open("a") as file:
        file.write(name + "\n")