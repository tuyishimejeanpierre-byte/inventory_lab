# Inventory Management System

## Project Overview

This project is a **Flask-based RESTful Inventory Management System** developed in Python. It allows users to manage inventory through a Command Line Interface (CLI) while exposing a REST API for CRUD (Create, Read, Update, Delete) operations. The application also integrates with the **OpenFoodFacts API** to retrieve product information using a barcode.

The project demonstrates RESTful API development, Object-Oriented Programming (OOP), JSON data storage, external API integration, unit testing, and Git workflow.

---

## Features

* View all inventory items
* View a single inventory item by ID
* Add new inventory items
* Update existing inventory items
* Delete inventory items
* Search products using the OpenFoodFacts API
* Command Line Interface (CLI)
* JSON file used as temporary database
* Unit tests for reusable components and CLI behavior

---

## Project Structure

```text
inventory_management/
│
├── app.py
├── config.py
├── db.json
├── requirements.txt
├── README.md
│
├── cli/
│   ├── __init__.py
│   └── cli.py
│
├── models/
│   ├── __init__.py
│   └── product.py
│
├── routes/
│   ├── __init__.py
│   ├── inventory_routes.py
│   └── external_routes.py
│
├── services/
│   ├── __init__.py
│   ├── inventory_service.py
│   └── openfood_service.py
│
├── utils/
│   ├── __init__.py
│   └── json_storage.py
│
└── tests/
    ├── __init__.py
    ├── test_cli.py
    ├── test_inventory_service.py
    └── test_json_storage.py
```

---

## Technologies Used

* Python 3
* Flask
* Requests
* JSON
* unittest
* pytest
* Git & GitHub

---

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Navigate into the project

```bash
cd inventory_management
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/macOS

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the Flask server:

```bash
python app.py
```

The API will run on:

```
http://127.0.0.1:5000
```

---

## Running the CLI

Open another terminal and run:

```bash
python cli/cli.py
```

The CLI allows users to:

* View inventory
* View a product
* Add a product
* Update a product
* Delete a product
* Search products using OpenFoodFacts

---

## API Endpoints

| Method | Endpoint                    | Description                        |
| ------ | --------------------------- | ---------------------------------- |
| GET    | `/inventory`                | Retrieve all inventory items       |
| GET    | `/inventory/<id>`           | Retrieve a single inventory item   |
| POST   | `/inventory`                | Create a new inventory item        |
| PATCH  | `/inventory/<id>`           | Update an inventory item           |
| DELETE | `/inventory/<id>`           | Delete an inventory item           |
| GET    | `/search?barcode=<barcode>` | Search product using OpenFoodFacts |

---

## Sample JSON Data

```json
{
  "inventory": [
    {
      "id": 1,
      "barcode": "5449000000996",
      "product_name": "Coca-Cola Original Taste",
      "brand": "Coca-Cola",
      "quantity": 20,
      "buying_price": 120,
      "selling_price": 150
    }
  ]
}
```

---

## Unit Testing

Run the test suite using **unittest**:

```bash
python -m unittest discover tests
```

Or using **pytest**:

```bash
pytest -v
```

---

## Object-Oriented Programming

The project follows OOP principles through:

* **Product** class representing inventory items.
* **InventoryService** containing business logic.
* **JSONStorage** handling data persistence.
* **OpenFoodService** managing communication with the external API.

---

## External API

The project integrates with the OpenFoodFacts API to retrieve product details using a barcode. The returned product information can be used to enrich the inventory data.

---

## Git Workflow

Development followed a feature-branch workflow:

* Create feature branch
* Develop feature
* Commit changes
* Merge into `develop`
* Delete merged feature branch

---

## Future Improvements

* Replace JSON storage with SQLite or PostgreSQL.
* Add user authentication and authorization.
* Implement input validation.
* Add logging and exception handling.
* Build a web-based frontend.
* Improve test coverage with integration tests.

---

