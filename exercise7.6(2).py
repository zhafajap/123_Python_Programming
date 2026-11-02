active = True

while active:
    topping = input("Enter a topping (or 'quit'): ")

    if topping == "quit":
        active = False
    else:
        print(f"I'll add {topping} to your pizza.")