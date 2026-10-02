"""Reusable order helpers kept separate from the script entry point."""


def describe_order(drink_name, quantity, unit_price):
    """Create a one-line description of an order and its total."""
    total = quantity * unit_price
    return f"{quantity} x {drink_name}: ${total:.2f}"
