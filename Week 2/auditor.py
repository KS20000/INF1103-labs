print("\nWelcome to Smart Inventory Auditor!\n")


inventory = 0
failed_entries = 0

while True:
    stock = input("Enter stock quantity (or 'quit' to exit): ")

    if stock == "quit":
        print("Total Units Processed: ", inventory)
        print("Number of Failed/Rejected Entries: ", failed_entries)
        break

    if not stock.isdigit():
        print("Error: Invalid input. Please enter a whole number.")
        failed_entries += 1
        continue

    stock = int(stock)

    if stock < 0:
        print("Error: Negative stock values are not allowed.")
        failed_entries += 1
        continue

    inventory += stock
    print("Stock added successfully.")

    if inventory > 500:
        print("ALERT: Overstock! Inventory exceeds 500 units.")
        break