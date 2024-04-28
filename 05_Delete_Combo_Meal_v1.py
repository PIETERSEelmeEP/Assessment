"""Ask user if they are certain they want to delete the combo, if yes, delete
the combo, and if no, deletion cancelled
"""

# Combo menu inside one large dictionary
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


# Asking the user if they are sure they want to delete the combo
def delete_verification(combo_delete, combo_items_):
    print(f"Combo Name: {combo_delete}")
    print("Items & Prices:")
    for item, price in combo_items_.items():
        print(f"{item}: ${price:.2f}")
    delete = input("\nAre you sure you want to delete this combo? "
                   "(yes/no) ").lower()
    if delete == "yes":
        # Delete combo
        del Combo_meals[combo_delete]
        print(f"\nCombo '{combo_delete}' deleted successfully!")
    else:
        print("Deletion canceled.")


# Searching for the combo the user wants to delete
def delete_combo():
    combo_delete = input("Enter the name of the combo you want to delete: ")

    if combo_delete in Combo_meals:
        combo_items_ = Combo_meals[combo_delete]
        delete_verification(combo_delete, combo_items_)
    else:
        print(f"There is no combo named '{combo_delete}'.")


# Print the Combo menu with format function
def print_combo_menu():
    for combo_name, items_prices in Combo_meals.items():
        print(f"\nCombo Name: {combo_name}\nItems & Prices:")

        for key in items_prices:
            print(f"{key}: {items_prices[key]}")


# Main Routine
delete_combo()
print_combo_menu()
