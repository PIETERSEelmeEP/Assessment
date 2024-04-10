"""Improve 03_Add_New_Combo_Meal_v1 by using easygui
"""
import easygui

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

# Create a dictionary for the new combo
combo_name = easygui.enterbox("Enter the name of the new combo meal",
                              title="Combo Name")
combo_items = {}
for _ in range(3):
    item_name = easygui.enterbox("Enter item name:", title="Item Name")

    # Testing to see if the price is an integer/float
    item_price_str = easygui.enterbox("Enter item price:", title="Item Price")
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

# printing the new list
print(Combo_meals)
