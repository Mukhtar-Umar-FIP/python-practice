"""Calculate and format an order using reusable functions."""


def calculate_total(price, quantity):
    """Return the cost of the requested number of drinks."""
    return price * quantity


def format_receipt(drink_name, quantity, total):
    """Return a short, readable receipt."""
    return f"{quantity} x {drink_name}: ${total:.2f}"


if __name__ == "__main__":
    # The total is calculated once, then passed to the receipt function.
    total = calculate_total(price=3.25, quantity=2)
    print(format_receipt("Iced tea", 2, total))
