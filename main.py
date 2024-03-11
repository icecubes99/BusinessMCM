import os

# Global Variables
inventory_file = "inventory.txt"
order_history_file = "order_history.txt"
inventory = {}
order_history = []

# Function to load inventory from file
def load_inventory():
    global inventory
    if os.path.exists(inventory_file):
        with open(inventory_file, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) != 3:
                    print(f"Skipping line '{line.strip()}': expected 3 values, got {len(parts)}")
                    continue
                product, quantity, price = parts
                inventory[product] = {"quantity": int(quantity), "price": float(price)}

# Function to save inventory to file
def save_inventory():
    with open(inventory_file, "w") as file:
        for product, details in inventory.items():
            file.write(f"{product},{details['quantity']},{details['price']}\n")

# Function to load order history from file
def load_order_history():
    global order_history
    if os.path.exists(order_history_file):
        with open(order_history_file, "r") as file:
            for line in file:
                order_history.append(line.strip())

#Function to save the order history to file     
def save_order(order):
    with open(order_history_file, "a") as file:
        file.write(f"{order}\n")

# Function to add a new product to the inventory
def add_product():
    print("\033[1m" + "Available Products:" + "\033[0m")# Bold text
    for product, details in inventory.items():
        print(f"{product}: {details['quantity']}")

    product_name = input("Enter the product name: ")
    if product_name in inventory:
        print("\033[1m" + "Product already exists." + "\033[0m")# Bold text
        return

    quantity = int(input("Enter the quantity: "))
    price = float(input("Enter the price: "))

    inventory[product_name] = {"quantity": quantity, "price": price}
    print("\033[1m" + "Product added successfully!" + "\033[0m")# Bold text

#Function to remove a product from the inventory
def remove_product():
    print("\033[1m" + "Available Products:" + "\033[0m")# Bold text
    for product, details in inventory.items():
        print(f"{product}: {details['quantity']}")

    product_name = input("Enter the product name to remove: ")
    if product_name in inventory:
        del inventory[product_name]
        print("\033[1m" + "Product removed successfully!" + "\033[0m")# Bold text
    else:
        print("\033[1m" + "Product not found." + "\033[0m")# Bold text

# Function to add stock
def add_stock():
    print("\033[1m" + "Available Products:" + "\033[0m")# Bold text
    for product, details in inventory.items():
        print(f"{product}: {details['quantity']}")

    product_name = input("Enter the product name to add stock: ")
    if product_name in inventory:
        quantity = int(input("Enter the quantity to add: "))
        inventory[product_name]["quantity"] += quantity
        print("\033[1m" + "Stock updated successfully!" + "\033[0m")# Bold text
    else:
        print("\033[1m" + "Product not found." + "\033[0m")# Bold text

# Function to remove stock
def remove_stock():
    print("\033[1m" + "Available Products:" + "\033[0m")# Bold text
    for product, details in inventory.items():
        print(f"{product}: {details['quantity']}")

    product_name = input("Enter the product name to remove stock: ")
    if product_name in inventory:
        quantity = int(input("Enter the quantity to remove: "))
        if inventory[product_name]["quantity"] >= quantity:
            inventory[product_name]["quantity"] -= quantity
            print("Stock updated successfully!")
        else:
            print("\033[1m" + "Insufficient stock." + "\033[0m")# Bold text
    else:
        print("\033[1m" + "Product not found." + "\033[0m")# Bold text

# Function to view product availability
def view_product_availability():
    print("\033[1m" + "Product Availability:" + "\033[0m")# Bold text
    for product, details in inventory.items():
        print(f"{product}: {details['quantity']}")

# Function to place order
def place_order():
    print("\033[1m" + "Available Products:" + "\033[0m")# Bold text
    for product, details in inventory.items():
        print(f"{product}: {details['quantity']}")
        
    product_name = input("Enter the product name to order: ")
    if product_name in inventory:
        quantity = int(input("Enter the quantity to order: "))
        if inventory[product_name]["quantity"] >= quantity:
            total_price = inventory[product_name]["price"] * quantity
            inventory[product_name]["quantity"] -= quantity
            order = f"Order: {quantity} \tProduct: {product_name} \tTotal Price: ${total_price}"
            order_history.append(order)
            print("Order placed successfully!")
            save_order(order) 
        else:
            print("\033[1m" + "Insufficient stock." + "\033[0m")
    else:
        print("\033[1m" + "Product not found." + "\033[0m") # Bold text

# Function to view order history
def view_order_history():
    print("\033[1m" + "Order History:" + "\033[0m")# Bold text
    for order in order_history:
        print(order)

# Dictionary to map menu options to functions
menu_options = {
    '1': add_stock,
    '2': remove_stock,
    '3': view_product_availability,
    '4': place_order,
    '5': view_order_history,
    '6': add_product,
    '7': remove_product,
    '8': lambda: exit(save_inventory()) # Exit function with save before exit
}

# Main Menu function
def main_menu():
    load_inventory()
    load_order_history()
    while True:
        print("\033[1m" + "\n--- Main Menu ---" + "\033[0m")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Product Availability")
        print("4. Place Order")
        print("5. View Order History")
        print("6. Add Product")
        print("7. Remove Product")
        print("8. Exit")

        choice = input("Enter your choice: ")

        # Check if the choice is in the menu options dictionary
        if choice in menu_options:
            # Call the corresponding function based on the choice
            menu_options[choice]()
        else:
            print("\033[1m" + "Invalid choice. Please try again." + "\033[0m")

# Execute the main menu
if __name__ == "__main__":
    main_menu()
