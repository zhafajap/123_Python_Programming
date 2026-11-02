#menggunakan break statement
while True:
    topping = input("Enter a topping (or 'quit'): ")

    if topping == "quit":
        break

    print(f"I'll add {topping} to your pizza.")