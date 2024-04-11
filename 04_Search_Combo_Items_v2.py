"""Search for combo names within the menu dictionary
"""


# Print the Combo menu with format function
def print_combo_menu():
    for combo_name, items_prices in Combo_meals.items():
        print(f"\nCombo Name: {combo_name}\nItems & Prices:")

        for key in items_prices:
            print(f"{key}: {items_prices[key]}")


# Menu dictionary
Combo_meals = {
    "Value": {
        "Beef Burger": 5.69,
        "Fries": 1.00,
        "Fizzy Drink": 1.00
    },
    "Cheezy": {
        "Cheeseburger": 6.69,
        "Fries": 1.00,
        "Fizzy Drink": 1.00
    },
    "Super": {
        "Cheeseburger": 6.69,
        "Large Fries": 2.00,
        "Smoothie": 2.00
    }
}


# Main Routine
def search_combo(combo_name):
    for combo, items in Combo_meals.items():
        if combo_name.lower() == combo.lower():
            return items
    return None

combo_name = input("Enter the name of the combo: ")
combo_items = search_combo(combo_name)

if combo_items:
    print(f"The combo '{combo_name}' includes the following items:")
    for item, price in combo_items.items():
        print(f"{item}: ${price:.2f}")
else:
    print(f"Combo '{combo_name}' not found.")

# printing the new list
print_combo_menu()
