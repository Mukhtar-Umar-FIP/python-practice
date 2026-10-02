"""Save and load a plain-text beverage receipt."""

from pathlib import Path


def save_receipt(receipt, file_path):
    """Write a receipt to a UTF-8 text file."""
    # UTF-8 handles common symbols consistently across operating systems.
    Path(file_path).write_text(receipt, encoding="utf-8")


def load_receipt(file_path):
    """Read a UTF-8 text receipt from a file."""
    return Path(file_path).read_text(encoding="utf-8")


if __name__ == "__main__":
    receipt_path = Path("beverage_receipt.txt")
    save_receipt("2 x Cappuccino: $7.00", receipt_path)
    print(load_receipt(receipt_path))
