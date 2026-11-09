from pathlib import Path
import json

path = Path("user_info.json")

user_info = {
    "first_name": input("Masukkan nama depan: "),
    "last_name": input("Masukkan nama belakang: "),
    "age": input("Masukkan umur: ")
}

contents = json.dumps(user_info)
path.write_text(contents)

loaded_info = json.loads(path.read_text())

print("\nInformasi yang diingat:")
print(f"Nama depan: {loaded_info['first_name']}")
print(f"Nama belakang: {loaded_info['last_name']}")
print(f"Umur: {loaded_info['age']}")