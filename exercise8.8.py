def make_album(artist, title):
    album = {
        "artist": artist,
        "title": title
    }

    return album


while True:
    print("\nEnter album information.")
    print("Enter 'q' to quit.")

    artist = input("Artist name: ")

    if artist == "q":
        break

    title = input("Album title: ")

    if title == "q":
        break

    album = make_album(artist, title)

    print(album)