"""Endpoint tests for the beverage products API."""

import pytest

from api_product.app import PRODUCTS, app


@pytest.fixture
def client():
    original_products = [product.copy() for product in PRODUCTS]
    app.config.update(TESTING=True)
    with app.test_client() as test_client:
        yield test_client
    PRODUCTS[:] = original_products


def test_health_and_get_all_products(client):
    health_response = client.get("/health")
    products_response = client.get("/products")

    assert health_response.status_code == 200
    assert health_response.get_json() == {"status": "ok"}
    assert products_response.status_code == 200
    assert products_response.get_json()[0]["name"] == "House coffee"


def test_get_one_product_and_unknown_product(client):
    found_response = client.get("/products/1")
    missing_response = client.get("/products/999")

    assert found_response.status_code == 200
    assert found_response.get_json()["category"] == "coffee"
    assert missing_response.status_code == 404
    assert missing_response.get_json() == {"error": "Product not found."}


def test_post_creates_product_with_server_assigned_id(client):
    response = client.post(
        "/products",
        json={"name": " Iced tea ", "category": " tea ", "price": 3.25},
    )

    assert response.status_code == 201
    assert response.get_json() == {
        "id": 3,
        "name": "Iced tea",
        "category": "tea",
        "price": 3.25,
    }
    assert client.get("/products/3").get_json()["name"] == "Iced tea"


def test_post_rejects_missing_name(client):
    response = client.post("/products", json={"category": "tea", "price": 2.0})

    assert response.status_code == 400
    assert response.get_json() == {"error": "Name must be a non-empty string."}


def test_post_rejects_missing_category(client):
    response = client.post("/products", json={"name": "Tea", "price": 2.0})

    assert response.status_code == 400
    assert response.get_json() == {"error": "Category must be a non-empty string."}


def test_post_rejects_negative_price(client):
    response = client.post(
        "/products",
        json={"name": "Tea", "category": "tea", "price": -1},
    )

    assert response.status_code == 400
    assert response.get_json() == {"error": "Price must be a non-negative number."}


def test_post_rejects_boolean_price(client):
    response = client.post(
        "/products",
        json={"name": "Tea", "category": "tea", "price": True},
    )

    assert response.status_code == 400
    assert response.get_json() == {"error": "Price must be a non-negative number."}


def test_post_requires_json_content_type(client):
    response = client.post("/products", data="not json", content_type="text/plain")

    assert response.status_code == 400
    assert response.get_json() == {"error": "Content-Type must be application/json."}


def test_post_rejects_non_object_json(client):
    response = client.post("/products", json=["not", "an", "object"])

    assert response.status_code == 400
    assert response.get_json() == {"error": "Request body must be a JSON object."}
