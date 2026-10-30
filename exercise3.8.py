places = ["Jepang", "Swiss", "Spanyol", "Korea Selatan", "Turki"]

# Menampilkan urutan asli
print(places)

# Mengurutkan sementara secara alfabetis
print(sorted(places))

# Membuktikan urutan asli tidak berubah
print(places)

# Mengurutkan sementara secara alfabetis terbalik
print(sorted(places, reverse=True))

# Membuktikan urutan asli tidak berubah
print(places)

# Membalik urutan list secara permanen
places.reverse()
print(places)

# Mengembalikan ke urutan semula
places.reverse()
print(places)

# Mengurutkan list secara alfabetis permanen
places.sort()
print(places)

# Mengurutkan list secara alfabetis terbalik permanen
places.sort(reverse=True)
print(places)