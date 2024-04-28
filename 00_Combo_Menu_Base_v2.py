"""Combined 01_Information_Welcome_Message_v2 and
02_Store_Original_Combo_Meals_v4 into one base program
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


# Welcome & Selected Action Function
def welcome_selected_action():
    # Welcome Message
    easygui.msgbox("Welcome", title="Welcome Message")

    # Select Action for Combo Menu Message & Buttonbox
    easygui.buttonbox("Please select action for the Combo Menu:",
                      title="Select Action", choices=["Add", "Search",
                                                      "Delete",
                                                      "Print Full Menu",
                                                      "Exit Program"])


# Print the Combo menu with format function
def print_combo_menu():
    for combo_name, items_prices in Combo_meals.items():
        print(f"\nCombo Name: {combo_name}\nItems & Prices:")

        for key in items_prices:
            print(f"{key}: {items_prices[key]}")


# Main Routine
welcome_selected_action()
print_combo_menu()
