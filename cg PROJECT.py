# Inventory dictionary
inventory = {}

# Function to add item
def add_item():
    name = input("Enter item name: ")
    if name in inventory:
        print(f"{name} already exists in inventory.\n")
        return
    price = float(input("Enter item price: "))
    quantity = int(input("Enter item quantity: "))
    category = input("Enter item category: ")
    inventory[name] = {"price": price, "quantity": quantity, "category": category}
    print(f"{name} has been added to the inventory.\n")

# Function to update item
def update_item():
    name = input("Enter the name of the item to update: ")
    if name in inventory:
        inventory[name]["price"] = float(input("Enter new price: "))
        inventory[name]["quantity"] = int(input("Enter new quantity: "))
        inventory[name]["category"] = input("Enter new category: ")
        print(f"{name} has been updated.\n")
    else:
        print(f"{name} not found in inventory.\n")

# Function to view inventory
def view_inventory():
    if not inventory:
        print("Inventory is empty.\n")
        return
    print("Inventory Items:")
    for name, details in inventory.items():
        print(f"Name: {name}, Price: ${details['price']}, Quantity: {details['quantity']}, Category: {details['category']}")
    print()

# Function to remove item
def remove_item():
    name = input("Enter the name of the item to remove: ")
    if name in inventory:
        del inventory[name]
        print(f"{name} has been removed from the inventory.\n")
    else:
        print(f"{name} not found in inventory.\n")

# Function to search by category
def search_by_category():
    category = input("Enter category to search: ")
    found_items = {name: details for name, details in inventory.items() if details["category"].lower() == category.lower()}
    if found_items:
        print(f"Items in category '{category}':")
        for name, details in found_items.items():
            print(f"Name: {name}, Price: ${details['price']}, Quantity: {details['quantity']}")
    else:
        print(f"No items found in category '{category}'.")
    print()

# Main loop
def main():
    while True:
        print("Inventory Management System")
        print("1. Add Item")
        print("2. Update Item")
        print("3. View Inventory")
        print("4. Remove Item")
        print("5. Search by Category")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_item()
        elif choice == "2":
            update_item()
        elif choice == "3":
            view_inventory()
        elif choice == "4":
            remove_item()
        elif choice == "5":
            search_by_category()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the program
if __name__ == "__main__":
    main()