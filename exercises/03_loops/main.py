"""Use loops to display a menu and total a multi-drink order."""

MENU = {"Coffee": 2.50, "Tea": 2.00, "Lemonade": 3.00}
ORDER = [("Coffee", 2), ("Tea", 1)]


def order_total(order):
    """Add the price of each drink in an order."""
    total = 0.0
    for drink_name, quantity in order:
        total += MENU[drink_name] * quantity
    return total


if __name__ == "__main__":
    print("Today's drinks:")
    # A loop visits each menu item without repeating print statements.
    for drink_name, price in MENU.items():
        print(f"{drink_name}: ${price:.2f}")
    print(f"Order total: ${order_total(ORDER):.2f}")
