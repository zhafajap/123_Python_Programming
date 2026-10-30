guest_list = [
    "Pedri",
    "Lionel Messi",
    "Lamine Yamal",
    "Kylian Mbappe",
    "Neymar",
    "Frenkie de Jong"]

# Memberitahu bahwa hanya dua orang yang bisa diundang
print("Maaf, saya hanya bisa mengundang dua orang untuk makan malam.")

# Menghapus tamu menggunakan pop()
guest = guest_list.pop()
print(f"Maaf {guest}, saya tidak bisa mengundang Anda.")

guest = guest_list.pop()
print(f"Maaf {guest}, saya tidak bisa mengundang Anda.")

guest = guest_list.pop()
print(f"Maaf {guest}, saya tidak bisa mengundang Anda.")

guest = guest_list.pop()
print(f"Maaf {guest}, saya tidak bisa mengundang Anda.")

# Memberitahu dua tamu yang masih diundang
print(f"{guest_list[0]}, Anda masih diundang untuk makan malam.")
print(f"{guest_list[1]}, Anda masih diundang untuk makan malam.")

# Menghapus dua nama yang tersisa
del guest_list[0]
del guest_list[0]

# Memastikan list sudah kosong
print(guest_list)