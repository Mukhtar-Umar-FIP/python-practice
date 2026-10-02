"""Small entry-point script that uses the reusable order helper."""

from .order_tools import describe_order


def main():
    """Print an example beverage order."""
    print(describe_order("Mocha", 1, 4.25))


# This guard lets us import main.py without starting the example program.
if __name__ == "__main__":
    main()
