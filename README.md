# Python Practice: Beverage Shop

This is a small Python practice project based on a simple beverage shop. It contains the eight exercises cover basic Python concepts, as well as a simple API for managing beverage products.

## Exercises

The exercises cover:

1. Variables and Data Types – Creating a simple drink order using different Python data types.
2. Conditionals – Using if statements to check shop hours and order quantities.
3. Loops – Displaying a menu and calculating the cost of drinks.
4. Functions – Using functions to calculate orders and create receipts.
5. Modules – Separating menu data and functions into different files.
6. Error Handling – Handling invalid user input.
7. File Handling – Saving and reading a simple receipt from a file.
8. Script Organisation – Organising code into reusable functions and a main program.

## API

The project also includes a simple Beverage Products API built with Flask.

It can:

Show all products
Show one product
Add a new product
Check that product information is valid
Return errors when something is wrong

The API stores products in memory, so new products will be lost when the server is restarted.

## Installing

The project uses Python 3.10 or newer.

Create a virtual environment:

py -m venv .venv
.venv\Scripts\Activate.ps1


Install the required packages:

python -m pip install -r requirements.txt

## Running the Exercises

For example:

python exercises/01_variables_data_types/main.py

The other exercises can be run in the same way.

## Running Tests

The project uses pytest for automated testing.

python -m pytest

There are tests for both the Python exercises and the API.

## Running the API

Run the API with:

python -m api_product.app

The API will run locally on:

http://127.0.0.1:5000

Example:

GET /products
GET /products/1
POST /products


## Engineering Decisions

I used Flask because it is simple and easy to understand.

I used in-memory data instead of a database to keep the project simple.

I used pytest to test the exercises and API.

I also used Waitress as a simple server that can be used when deploying the API.
