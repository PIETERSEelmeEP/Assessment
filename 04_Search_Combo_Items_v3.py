"""Improving 04_Search_Combo_Items_v2 and placing them in a function to reuse
later on in the program
"""


def print_search_results(combo, combo_items):
    print("\nResults:")
    print(f"Combo Name: {combo}")
    print("Items & Prices:")
    for item_, price in combo_items.items():
        print(f"{item_}: ${price:.2f}")


def search_in_combo():
    combo_search = input("Enter the name of the combo you are searching for: ")
    found = False

    # Searching for the Combo
    for combo, combo_items in Combo_meals.items():
        if combo_search.lower() == combo.lower():
            print_search_results(combo, combo_items)
            found = True
        else:
            for item in combo_items:
                if combo_search.lower() == item.lower():
                    print_search_results(combo, combo_items)
                    found = True

    if not found:
        print(f"There are no Combos named {combo_search}\nNor are there any "
              f"items "
              f"within Combos named {combo_search}")


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
search_in_combo()
