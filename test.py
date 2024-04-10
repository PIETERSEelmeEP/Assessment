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

for combo_name, items_prices in Combo_meals.items():
    print(f"\nCombo Name: {combo_name}\nItems & Prices:")

    for key in items_prices:
        print(f"{key}: {items_prices[key]}")

---------------------------------------------------------------------------

import easygui

# Get the input as a string
input_str = easygui.enterbox("Enter ID:", title="Contact ID")

# Convert the input to a float with two decimal places
try:
    contact_ID = "{:.2f}".format(float(input_str))
    easygui.msgbox(f"Contact ID: {contact_ID}")
except ValueError:
    easygui.msgbox("Invalid input! Please enter a valid number.")
