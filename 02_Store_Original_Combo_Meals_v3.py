"""Create dictionaries within nested dictionaries. These are the original combo
menu, consisting of items with each item's price
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

# Print the Combo menu with format
for combo_name, items_prices in Combo_meals.items():
    print(f"\nCombo Name: {combo_name}\nItems & Prices:")

    for key in items_prices:
        print(f"{key}: {items_prices[key]}")
