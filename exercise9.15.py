from random import choice

lottery_items = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    "A", "B", "C", "D", "E"
]

my_ticket = [1, "A", 5, "C"]

winning_ticket = []
attempts = 0

while winning_ticket != my_ticket:
    winning_ticket = []

    while len(winning_ticket) < 4:
        item = choice(lottery_items)

        if item not in winning_ticket:
            winning_ticket.append(item)

    attempts += 1

print(f"Tiket saya: {my_ticket}")
print(f"Tiket pemenang: {winning_ticket}")
print(f"Jumlah percobaan: {attempts}")