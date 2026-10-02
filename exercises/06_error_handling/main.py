"""Convert user input while handling common input errors."""


def read_quantity(value):
    """Return a valid positive quantity or a helpful error message."""
    # int() raises ValueError when the entered text is not a whole number.
    try:
        quantity = int(value)
    except ValueError:
        return None, "Enter a whole number."

    if quantity <= 0:
        return None, "Quantity must be greater than zero."
    return quantity, ""


if __name__ == "__main__":
    entered_value = input("How many drinks would you like? ")
    quantity, error = read_quantity(entered_value)
    if error:
        print(error)
    else:
        print(f"Thanks, your order is for {quantity} drink(s).")
