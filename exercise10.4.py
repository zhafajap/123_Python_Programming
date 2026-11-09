from pathlib import Path

name = input("Masukkan nama kamu: ")

path = Path("guest.txt")
path.write_text(name)

print(f"Halo, {name}! Nama kamu sudah disimpan.")