import json
import os

from inventory import Inventory
from product import Product

INVENTORY_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "inventory.json")


def load_inventory():
    inventory = Inventory()
    if not os.path.exists(INVENTORY_FILE):
        print("inventory.json not found. Starting with an empty inventory.")
        return inventory

    try:
        with open(INVENTORY_FILE, "r", encoding="utf-8") as file:
            records = json.load(file)
        if not isinstance(records, list):
            raise ValueError("Inventory file must contain a list.")
        for record in records:
            inventory.add_product(Product.from_dict(record))
        print("Inventory loaded successfully.")
    except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
        print(f"Could not load inventory.json ({error}). Starting with an empty inventory.")
        return Inventory()
    return inventory


def save_inventory(inventory):
    try:
        with open(INVENTORY_FILE, "w", encoding="utf-8") as file:
            json.dump([product.to_dict() for product in inventory.get_products()], file, indent=4)
        print("Inventory saved successfully to inventory.json.")
    except OSError:
        print("Error: inventory could not be saved.")


def add_product(inventory):
    print("\nAdd New Product")
    product_id = input("Product ID: ").strip()
    name = input("Product Name: ").strip()
    try:
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))
        inventory.add_product(Product(product_id, name, price, stock))
        print("\nProduct added successfully!")
    except ValueError as error:
        print(error)


def update_stock(inventory):
    print("\nUpdate Stock")
    product = inventory.search_product(input("Enter Product ID: ").strip())
    if product is None:
        print("\nProduct not found.")
        return

    print("\nProduct Found:")
    print(f"Name: {product.name}")
    print(f"Current Stock: {product.stock}")
    try:
        product.update_stock(int(input("New Stock Quantity: ")))
        print("Stock updated successfully!")
    except ValueError:
        print("Stock must be a non-negative whole number.")


def search_product(inventory):
    print("\nSearch Product")
    product = inventory.search_product(input("Enter Product ID: ").strip())
    if product is None:
        print("Product not found.")
        return
    print("Product Found")
    print("------------------------------------------------")
    product.display_information()
    print("------------------------------------------------")


def main():
    inventory = load_inventory()
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
            inventory.display_all()
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


if __name__ == "__main__":
    main()
