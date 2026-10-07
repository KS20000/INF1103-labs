import json
import os

INVENTORY_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "inventory.json"
)

def add_product(products):
    print("\nAdd New Product")

    product_id = input("Product ID: ").strip().upper()

    if search_product(products, product_id, announce=False):
        print("A product with that ID already exists.")
        return

    name = input("Product Name: ").strip()

    try:
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))

        if not name or price < 0 or stock < 0:
            raise ValueError
    except ValueError:
        print("Enter a product name, a non-negative price, and a non-negative whole-number stock quantity.")
        return

    products.append({
        "id": product_id,
        "name": name,
        "price": price,
        "stock": stock
    })

    print("\nProduct added successfully!")


def update_stock(products):
    print("\nUpdate Stock")
    product_id = input("Enter Product ID: ").strip().upper()
    product = search_product(products, product_id, announce=False)

    if product is None:
        print("\nProduct not found.")
        return

    print("\nProduct Found:")
    print(f"Name: {product['name']}")
    print(f"Current Stock: {product['stock']}")

    try:
        new_stock = int(input("New Stock Quantity: "))
        if new_stock < 0:
            raise ValueError
    except ValueError:
        print("Stock must be a non-negative whole number.")
        return

    product["stock"] = new_stock
    print("Stock updated successfully!")


def search_product(products, product_id=None, announce=True):
    if product_id is None:
        print("\nSearch Product")
        product_id = input("Enter Product ID: ").strip().upper()

    for product in products:
        if product["id"].upper() == product_id.upper():
            if announce:
                print("Product Found")
                print("------------------------------------------------")
                print(f"ID: {product['id']}")
                print(f"Name: {product['name']}")
                print(f"Price: ${product['price']:.2f}")
                print(f"Stock: {product['stock']}")
                print("------------------------------------------------")
            return product

    if announce:
        print("Product not found.")

    return None


def display_all(products):
    print("\nCurrent Inventory")
    print("------------------------------------------------")

    if not products:
        print("No products in inventory.")
    else:
        for product in products:
            print(
                f"ID: {product['id']} | "
                f"Name: {product['name']} | "
                f"Price: ${product['price']:.2f} | "
                f"Stock: {product['stock']}"
            )

    print("------------------------------------------------")


def load_inventory():
    if os.path.exists(INVENTORY_FILE):
        print("inventory.json found.")

        try:
            with open(INVENTORY_FILE, "r") as file:
                products = json.load(file)

            print("Inventory loaded successfully.")
            return products

        except (json.JSONDecodeError, OSError):
            print("Could not read inventory.json. Starting with an empty inventory.")
            return []

    print("inventory.json not found. Starting with an empty inventory.")
    return []


inventory = load_inventory()


def save_inventory(products):
    try:
        with open(INVENTORY_FILE, "w") as file:
            json.dump(products, file, indent=4)

        print("Inventory saved successfully to inventory.json.")
    except OSError:
        print("Error: inventory could not be saved.")


while True:
    print("\n----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")

    choice = input("Enter option: ").strip()

    if choice == "1":
        display_all(inventory)
    elif choice == "2":
        add_product(inventory)
    elif choice == "3":
        update_stock(inventory)
    elif choice == "4":
        search_product(inventory)
    elif choice == "5":
        print("\nSaving inventory...")
        save_inventory(inventory)
    elif choice == "6":
        print("\nSaving inventory before exit...")
        save_inventory(inventory)
        print("Thank you for using Inventory Management System.")
        print("Program terminated.")
        break
    else:
        print("Invalid option. Enter a number from 1 to 6.")