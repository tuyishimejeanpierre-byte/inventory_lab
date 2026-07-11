import requests


BASE_URL = "http://127.0.0.1:5000"


def menu():
    print("""
=============================
 INVENTORY MANAGEMENT CLI
=============================

1. View Inventory
2. View Single Product
3. Add Product
4. Update Product
5. Delete Product
6. Search Product (OpenFoodFacts)
7. Exit
""")


def view_inventory():
    res = requests.get(f"{BASE_URL}/inventory")
    
    data = res.json()
    print(data)
    return data


def view_product():
    product_id = input("Enter product ID: ")
    res = requests.get(f"{BASE_URL}/inventory/{product_id}")
    print(res.json())


def add_product():
    data = {
        "barcode": input("Barcode: "),
        "product_name": input("Product Name: "),
        "brand": input("Brand: "),
        "quantity": int(input("Quantity: ")),
        "buying_price": float(input("Buying Price: ")),
        "selling_price": float(input("Selling Price: "))
    }

    res = requests.post(f"{BASE_URL}/inventory", json=data)
    print(res.json())


def update_product():
    product_id = input("Enter product ID: ")

    print("Leave blank if no change")

    data = {}

    barcode = input("Barcode: ")
    if barcode:
        data["barcode"] = barcode

    product_name = input("Product Name: ")
    if product_name:
        data["product_name"] = product_name

    brand = input("Brand: ")
    if brand:
        data["brand"] = brand

    quantity = input("Quantity: ")
    if quantity:
        data["quantity"] = int(quantity)

    buying_price = input("Buying Price: ")
    if buying_price:
        data["buying_price"] = float(buying_price)

    selling_price = input("Selling Price: ")
    if selling_price:
        data["selling_price"] = float(selling_price)

    res = requests.patch(
        f"{BASE_URL}/inventory/{product_id}",
        json=data
    )

    print(res.json())


def delete_product():
    product_id = input("Enter product ID: ")
    res = requests.delete(f"{BASE_URL}/inventory/{product_id}")
    print(res.json())


def search_product():
    barcode = input("Enter barcode: ")

    res = requests.get(f"{BASE_URL}/search?barcode={barcode}")

    if res.status_code != 200:
        print(res.json())
        return

    product = res.json()

    print("\nProduct Found")
    print("----------------------")
    print(f"Barcode: {product['barcode']}")
    print(f"Name: {product['product_name']}")
    print(f"Brand: {product['brand']}")
    print(f"Ingredients: {product['ingredients']}")

    choice = input("\nAdd this product to inventory? (y/n): ")

    if choice.lower() != "y":
        return

    quantity = int(input("Quantity: "))
    buying_price = float(input("Buying Price: "))
    selling_price = float(input("Selling Price: "))

    inventory_item = {
        "barcode": product["barcode"],
        "product_name": product["product_name"],
        "brand": product["brand"],
        "quantity": quantity,
        "buying_price": buying_price,
        "selling_price": selling_price
    }

    add = requests.post(
        f"{BASE_URL}/inventory",
        json=inventory_item
    )

    print(add.json())

def main():

    while True:
        menu()
        choice = input("Choose an option: ")

        if choice == "1":
            view_inventory()

        elif choice == "2":
            view_product()

        elif choice == "3":
            add_product()

        elif choice == "4":
            update_product()

        elif choice == "5":
            delete_product()

        elif choice == "6":
            search_product()

        elif choice == "7":
            print("Exiting...")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()