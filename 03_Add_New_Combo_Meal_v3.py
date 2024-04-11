"""Improve 03_Add_New_Combo_Meal_v2 by formatting the printed results
"""
import easygui


def add_combo():
    # Create a dictionary for the new combo
    combo_name = easygui.enterbox("Enter the name of the new combo meal",
                                  title="Combo Name")
    combo_items = {}
    for _ in range(3):
        item_name = easygui.enterbox("Enter item name:", title="Item Name")

        # Testing to see if the price is an integer/float
        item_price_str = easygui.enterbox("Enter item price:",
                                          title="Item Price")
        try:
            item_price = float(item_price_str)
        except ValueError:
            easygui.msgbox("Must be an integer", title="Error Message")
            item_price_str = easygui.enterbox("Please enter a price:",
                                              title="Item Price")
            item_price = float(item_price_str)

        combo_items[item_name] = item_price

    # Moving the new dictionary within the Combo meals dictionary
    Combo_meals[combo_name] = combo_items


# Print the Combo menu with format function
def print_combo_menu():
    for combo_name, items_prices in Combo_meals.items():
        print(f"\nCombo Name: {combo_name}\nItems & Prices:")

        for key in items_prices:
            print(f"{key}: {items_prices[key]}")


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
# printing the new list
add_combo()
print_combo_menu()
