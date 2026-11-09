from pathlib import Path

filename = "alice.txt"

path = Path(filename)

try:
    contents = path.read_text(encoding="utf-8")
    word_count = contents.lower().count("the")

    print(f"Jumlah kata 'the' dalam file: {word_count}")

except FileNotFoundError:
    print(f"File {filename} tidak ditemukan.")