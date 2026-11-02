def make_sandwich(*items):
    """Print a summary of the sandwich being ordered."""
    print("\nMaking a sandwich with:")

    for item in items:
        print(f"- {item}")


make_sandwich("Cheese", "Beef")
make_sandwich("Egg", "Lettuce", "Tomato")
make_sandwich("Chicken", "Cheese", "Mayonnaise")