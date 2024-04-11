"""Search for combo names within the menu dictionary
"""

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
combo_search = input("Enter the name of the combo you are searching for: ")

# Searching for the Combo
found = False
for combo, items in Combo_meals.items():
    if combo_search.lower() == combo.lower():
        print("Results:")
        print(f"Combo Name: {combo_search}")
        print("Items & Prices:")
        for item, price in items.items():
            print(f"{item}: ${price:.2f}")
        found = True
        break

if not found:
    print(f"There are no Combos named {combo_search}")
