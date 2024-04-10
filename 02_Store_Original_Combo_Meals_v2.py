"""These are the original combo menu, consisting of items with each item's
price (Using Dictionary in a List)
"""

# dictionary inside the combo menu list
menu = [
    {"Combo Name": "Value", "Combo Items": {"Beef Burger": 5.69, "Fries": 1.00,
                                            "Fizzy Drink": 1.00}},
    {"Combo Name": "Cheezy", "Combo Items": {"Cheeseburger": 6.69,
                                             "Fries": 1.00,
                                             "Fizzy Drink": 1.00}},
    {"Combo Name": "Super", "Combo Items": {"Cheeseburger": 6.69,
                                            "Large Fries": 2.00,
                                            "Smoothie": 2.00}}
]

# Print the Combo menu with format
for combo in menu:
    combo_name = combo["Combo Name"]
    combo_items = combo["Combo Items"]
    print(f"Combo Name: {combo_name}")
    for item, price in combo_items.items():
        print(f"\t{item}: {price:.2f}")
