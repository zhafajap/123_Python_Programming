from pathlib import Path
import json


def get_stored_username(path):
    if path.exists():
        contents = path.read_text()
        return json.loads(contents)

    return None


def get_new_username(path):
    username = input("Siapa nama kamu? ")
    contents = json.dumps(username)
    path.write_text(contents)

    return username


def greet_user():
    path = Path("username.json")

    username = get_stored_username(path)

    if username:
        answer = input(
            f"Apakah nama kamu {username}? (y/n): "
        )

        if answer.lower() == "y":
            print(f"Selamat datang kembali, {username}!")

        else:
            username = get_new_username(path)
            print(f"Kami akan mengingat kamu, {username}!")

    else:
        username = get_new_username(path)
        print(f"Kami akan mengingat kamu, {username}!")


greet_user()