def make_album(artist, title, songs=None):
    album = {
        "artist": artist,
        "title": title
    }

    if songs is not None:
        album["songs"] = songs

    return album


album1 = make_album("Taylor Swift", "1989")
album2 = make_album("The Weeknd", "After Hours")
album3 = make_album("Joji", "Nectar")
album4 = make_album("The 1975", "Being Funny in a Foreign Language", 10)

print(album1)
print(album2)
print(album3)
print(album4)