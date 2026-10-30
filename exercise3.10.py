players = ["Messi", "Ronaldo", "Neymar", "Mbappe"]

# Menampilkan list
print(players)

# Mengakses elemen berdasarkan indeks
print(players[0])

# Mengubah elemen
players[1] = "Pedri"
print(players)

# Menambahkan elemen di akhir
players.append("Yamal")
print(players)

# Menambahkan elemen pada posisi tertentu
players.insert(1, "Frenkie")
print(players)

# Menghapus elemen menggunakan del
del players[2]
print(players)

# Menghapus elemen menggunakan pop()
players.pop()
print(players)

# Menghapus elemen berdasarkan nilai
players.remove("Neymar")
print(players)

# Mengurutkan sementara
print(sorted(players))

# Membalik urutan
players.reverse()
print(players)

# Mengurutkan permanen
players.sort()
print(players)

# Mengurutkan terbalik
players.sort(reverse=True)
print(players)

# Menghitung jumlah elemen
print(len(players))