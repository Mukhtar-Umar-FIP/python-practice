"""Choose a simple order message with conditional branches."""


def order_message(shop_is_open, quantity):
    """Return a message for the shop's current order situation."""
    # Check the invalid quantity before checking whether the shop is open.
    if quantity <= 0:
        return "Choose at least one drink."
    if not shop_is_open:
        return "The shop is closed. Please come back later."
    return f"Your order for {quantity} drink(s) is being prepared."


if __name__ == "__main__":
    print(order_message(shop_is_open=True, quantity=2))
