"""Improving 04_Search_Combo_Items_v1 and allowing for the user to not only
search for a combo name but for an item
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
found = False

# Searching for the Combo
for combo, combo_items in Combo_meals.items():
    if combo_search.lower() == combo.lower():
        print("\nResults:")
        print(f"Combo Name: {combo}")
        print("Items & Prices:")
        for item, price in combo_items.items():
            print(f"{item}: ${price:.2f}")
        found = True
    else:
        for item in combo_items:
            if combo_search.lower() == item.lower():
                print("\nResults:")
                print(f"Combo Name: {combo_search}")
                print("Items & Prices:")
                for item_, price in combo_items.items():
                    print(f"{item_}: ${price:.2f}")
                found = True

if not found:
    print(f"There are no Combos named {combo_search}\nNor are there any items "
          f"within Combos named {combo_search}")
