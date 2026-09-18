# Smart Inventory Auditor - Modular Version

# Gets and validates the user's stock input.
# Returns an integer for valid input, "quit" to exit,
# or None for an invalid input.
def get_valid_input():
    stock = input("Enter stock quantity (or 'quit' to exit): ")

    if stock == "quit":
        return "quit"

    if not stock.isdigit():
        print("Error: Invalid input. Please enter a whole number.")
        return None

    return int(stock)


# Adds a new delivery amount to the current inventory total.
# Returns the updated inventory total.
def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total


# Calculates 10% tax for a specific delivery.
# Returns the calculated tax amount.
def calculate_tax(amount):
    tax = amount * 0.10
    return tax


# Prints the final inventory report.
def generate_report(total_units, failed_attempts, inventory):
    print("\n--- Final Report ---")
    print("Total Deliveries Processed:", total_units)
    print("Total Stock Processed:", inventory)
    print("Number of Failed/Rejected Entries:", failed_attempts)


# Main program

print("\nWelcome to Smart Inventory Auditor!\n")

inventory = 0
failed_attempts = 0
deliveries_processed = 0

while True:

    stock = get_valid_input()

    # Exit the program if the user enters "quit".
    if stock == "quit":
        generate_report(deliveries_processed, failed_attempts, inventory)
        break

    # Invalid input is rejected.
    if stock is None:
        failed_attempts += 1
        continue

    # Check whether adding the new delivery would exceed 500 units.
    if inventory + stock > 500:
        print("ALERT: Overstock! Delivery rejected.")
        print("The stock was NOT added to the inventory.\n")
        failed_attempts += 1
        generate_report(deliveries_processed, failed_attempts, inventory)
        break

    # Process the valid delivery.
    inventory = process_delivery(inventory, stock)

    # Calculate tax for this specific delivery.
    tax = calculate_tax(stock)

    deliveries_processed += 1

    print("\nSuccess! Stock added successfully.")
    print("Delivery Amount:", stock)
    print("Tax (10%):", tax)
    print("Total current stock:", inventory)