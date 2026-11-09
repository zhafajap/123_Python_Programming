from pathlib import Path

filenames = ["cats.txt", "dogs.txt"]

for filename in filenames:
    path = Path(filename)

    try:
        contents = path.read_text()
        print(contents)

    except FileNotFoundError:
        pass