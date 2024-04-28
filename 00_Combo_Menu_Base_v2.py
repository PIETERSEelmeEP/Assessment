"""Combined 00_Combo_Menu_Base_v1, 03_Add_New_Combo_Meal_v3,
04_Search_Combo_Items_4 and 05_Delete_Combo_Meal_v2 into a single program.
I also placed it in a loop so the program repeats until user chooses to exit
program
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


# Add Combo function
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


# Print search results function
def print_search_results(combo, combo_items):
    found_it = "Results:\n"
    found_it += f"Combo Name: {combo}\nItems & Prices:\n"
    for item_, price in combo_items.items():
        found_it += f"{item_}: ${price:.2f}\n"

    easygui.msgbox(found_it, title="Search Results")


# Search for combo in dictionary function
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


# Welcome & Selected Action Function
def welcome_selected_action():
    # Welcome Message
    easygui.msgbox("Welcome", title="Welcome Message")

    # Select Action for Combo Menu Message & Buttonbox
    while True:
        choice = easygui.buttonbox("Please select action for the Combo Menu:",
                                   title="Select Action",
                                   choices=["Add", "Search", "Delete",
                                            "Print Full Menu", "Exit Program"])
        if choice == "Add":
            add_combo()
        elif choice == "Search":
            search_in_combo()
        elif choice == "Delete":
            delete_combo()
        elif choice == "Print Full Menu":
            print_combo_menu()
        else:
            return


# Main Routine
welcome_selected_action()
