"""Add a new combo meal to the menu
"""

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
combo_name = input("Enter the name of the new combo meal: ")
combo_items = {}
for _ in range(3):
    item_name = input("Enter item name: ")
    item_price = float(input("Enter item price: "))
    combo_items[item_name] = item_price

# Moving the new dictionary within the Combo meals dictionary
Combo_meals[combo_name] = combo_items

# printing the new list
print(Combo_meals)
