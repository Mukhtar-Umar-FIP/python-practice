"""Menu data and lookup helpers for the module exercise."""

# Keep menu data here so other modules can import and reuse it.
DRINKS = {"Latte": 3.75, "Green tea": 2.25, "Hot chocolate": 3.50}


def price_for(drink_name):
    """Return a drink's price, or None when it is not on the menu."""
    return DRINKS.get(drink_name)
