topping = ""

while topping != "quit":
    topping = input("Enter a topping (or 'quit'): ")

    if topping != "quit":
        print(f"I'll add {topping} to your pizza.")