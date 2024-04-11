"""Improving 04_Search_Combo_Items_v3 using easygui
"""
import easygui


def print_search_results(combo, combo_items):
    results_msg = f"Results:\nCombo Name: {combo}\nItems & Prices:\n"
    for item_, price in combo_items.items():
        results_msg += f"{item_}: ${price:.2f}\n"
    easygui.msgbox(results_msg, title="Search Results")


def search_in_combo():
    combo_search = easygui.enterbox("Enter the name of the combo you are "
                                    "searching for:", title="Searching")
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
        easygui.msgbox(f"There are no Combos named {combo_search}\nNor are "
                       f"there any items within Combos named {combo_search}",
                       title="No Results")


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
