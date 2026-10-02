"""A JSON API for browsing and adding beverage products."""

from flask import Flask, jsonify, request

app = Flask(__name__)

PRODUCTS = [
    {"id": 1, "name": "House coffee", "category": "coffee", "price": 2.50},
    {"id": 2, "name": "Green tea", "category": "tea", "price": 2.25},
]


@app.get("/health")
def health():
    """Report that the API process is ready to answer requests."""
    return jsonify({"status": "ok"})


@app.get("/products")
def get_products():
    """Return all products as a JSON list."""
    return jsonify(PRODUCTS)


@app.get("/products/<int:product_id>")
def get_product(product_id):
    """Return one product, or a JSON 404 response."""
    product = None
    for item in PRODUCTS:
        if item["id"] == product_id:
            product = item
            break

    if product is None:
        return jsonify({"error": "Product not found."}), 404
    return jsonify(product)


@app.post("/products")
def create_product():
    """Validate and add a product, returning the created JSON object."""
    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json."}), 400

    product_data = request.get_json(silent=True)
    if not isinstance(product_data, dict):
        return jsonify({"error": "Request body must be a JSON object."}), 400

    name = product_data.get("name")
    category = product_data.get("category")
    price = product_data.get("price")

    if not isinstance(name, str) or not name.strip():
        return jsonify({"error": "Name must be a non-empty string."}), 400
    if not isinstance(category, str) or not category.strip():
        return jsonify({"error": "Category must be a non-empty string."}), 400
    if isinstance(price, bool) or not isinstance(price, (int, float)) or price < 0:
        return jsonify({"error": "Price must be a non-negative number."}), 400

    new_product = {
        "id": max((item["id"] for item in PRODUCTS), default=0) + 1,
        "name": name.strip(),
        "category": category.strip(),
        "price": float(price),
    }
    PRODUCTS.append(new_product)
    return jsonify(new_product), 201


if __name__ == "__main__":
    app.run(debug=True)
