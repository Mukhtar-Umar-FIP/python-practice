"""Behavior checks for the beginner exercise examples."""

import importlib


def test_conditionals_choose_expected_order_message():
    exercise = importlib.import_module("exercises.02_conditionals.main")

    assert exercise.order_message(True, 2) == "Your order for 2 drink(s) is being prepared."
    assert exercise.order_message(False, 2) == "The shop is closed. Please come back later."
    assert exercise.order_message(True, 0) == "Choose at least one drink."


def test_loops_calculate_multiple_drinks():
    exercise = importlib.import_module("exercises.03_loops.main")

    assert exercise.order_total([("Coffee", 2), ("Tea", 1)]) == 7.0


def test_functions_calculate_and_format_receipt():
    exercise = importlib.import_module("exercises.04_functions.main")

    total = exercise.calculate_total(3.25, 2)
    assert total == 6.5
    assert exercise.format_receipt("Iced tea", 2, total) == "2 x Iced tea: $6.50"


def test_modules_find_known_and_unknown_drinks():
    menu = importlib.import_module("exercises.05_modules.beverage_menu")

    assert menu.price_for("Latte") == 3.75
    assert menu.price_for("Water") is None


def test_error_handling_returns_clear_results():
    exercise = importlib.import_module("exercises.06_error_handling.main")

    assert exercise.read_quantity("3") == (3, "")
    assert exercise.read_quantity("many") == (None, "Enter a whole number.")
    assert exercise.read_quantity("0") == (None, "Quantity must be greater than zero.")


def test_file_handling_round_trips_receipt(tmp_path):
    exercise = importlib.import_module("exercises.07_file_handling.main")
    file_path = tmp_path / "receipt.txt"

    exercise.save_receipt("1 x Tea: $2.00", file_path)

    assert exercise.load_receipt(file_path) == "1 x Tea: $2.00"


def test_script_organisation_formats_order():
    tools = importlib.import_module("exercises.08_script_organisation.order_tools")

    assert tools.describe_order("Mocha", 2, 4.25) == "2 x Mocha: $8.50"
