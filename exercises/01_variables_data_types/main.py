"""Store and display a simple beverage order."""

drink_name = "Cappuccino"  # str
quantity = 2  # int
price_each = 3.50  # float
is_iced = False  # bool
extras = ["oat milk", "cinnamon"]  # list[str]

order_total = quantity * price_each

print(f"Drink: {drink_name}")
print(f"Quantity: {quantity}")
print(f"Iced: {is_iced}")
print(f"Extras: {', '.join(extras)}")
print(f"Total: ${order_total:.2f}")
