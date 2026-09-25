# Order Management System - Persistent Version

# Gets and validates the user's product name and quantity.
# Returns the product name and quantity.

def get_valid_input():
    product_name = input("\nEnter Product Name: ")
    quantity = int(input("Enter Quantity: "))

    return product_name, quantity


# Creates a new order.
# Returns the new order.

def process_order(order_id, product_name, quantity):
    new_order = (order_id, product_name, quantity)
    return new_order


# Prints the current orders.

def generate_report(orders):
    print("\nCurrent Orders:")

    for order in orders:
        print(f"{order[0]}, {order[1]}, {order[2]}")


# Loads the previous orders from orders.txt.
# If orders.txt does not exist, starts with an empty order list.

def load_orders():
    orders = []

    try:
        with open("orders.txt", "r") as file:

            for line in file:
                order = line.strip().split(", ")

                order_id = int(order[0])
                product_name = order[1]
                quantity = int(order[2])

                orders.append((order_id, product_name, quantity))

        return orders

    except FileNotFoundError:
        return []


# Saves the new order to orders.txt.

def save_order(order):
    with open("orders.txt", "a") as file:
        file.write(
            str(order[0]) + ", " +
            str(order[1]) + ", " +
            str(order[2]) + "\n"
        )


# Main program

print("\nWelcome to Order Management System!\n")

orders = load_orders()

generate_report(orders)

# Start order ID at 1001.
if len(orders) == 0:
    order_id = 1001
else:
    order_id = orders[-1][0] + 1

# Get product name and quantity.
product_name, quantity = get_valid_input()

# Create the new order.
new_order = process_order(
    order_id,
    product_name,
    quantity
)

print(
    "\nNew Order Added:",
    new_order[0],
    ",",
    new_order[1],
    ",",
    new_order[2]
)

# Save the new order.
save_order(new_order)

print("\nOrder successfully saved to orders.txt")