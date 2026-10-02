"""Import and display data from the beverage_menu module."""

from .beverage_menu import DRINKS


def main():
    """Print all drinks provided by the menu module."""
    for drink_name, price in DRINKS.items():
        print(f"{drink_name}: ${price:.2f}")


if __name__ == "__main__":
    main()
