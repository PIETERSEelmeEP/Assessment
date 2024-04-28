"""Improved 05_Delete_Combo_Meal_v1 using easygui
"""
import easygui

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
    delete_it = f"\nCombo Name: {combo_delete}"
    delete_it += "\nItems & Prices:"
    for item, price in combo_items_.items():
        delete_it += f"\n{item}: ${price:.2f}"
    delete = easygui.buttonbox(f"Do you want to delete:(yes/no)\n{delete_it}",
                               title="Delete Verification",
                               choices=["Yes", "No"])
    if delete == "Yes":
        # Delete combo
        del Combo_meals[combo_delete]
        easygui.msgbox(f"\nCombo '{combo_delete}' deleted successfully!",
                       title="Deletion Verified")
    else:
        easygui.msgbox("Deletion cancelled", title="Deletion Cancelled")


# Searching for the combo the user wants to delete
def delete_combo():
    combo_delete = easygui.enterbox("Enter the name of the combo you want to "
                                    "delete:", title="Delete Combo")

    if combo_delete in Combo_meals:
        combo_items_ = Combo_meals[combo_delete]
        delete_verification(combo_delete, combo_items_)
    else:
        easygui.msgbox(f"There is no combo named '{combo_delete}'.")


# Print the Combo menu with format function
def print_combo_menu():
    for combo_name, items_prices in Combo_meals.items():
        print(f"\nCombo Name: {combo_name}\nItems & Prices:")

        for key in items_prices:
            print(f"{key}: {items_prices[key]}")


# Main Routine
delete_combo()
print_combo_menu()
