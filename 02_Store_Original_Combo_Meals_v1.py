"""These are the original combo menu, consisting of items with each item's
price (Using Dictionary Lists)
"""

# Combo menu inside one large list
menu = [
    ["Value", {"Beef Burger": 5.69, "Fries": 1.00, "Fizzy Drink": 1.00}],
    ["Cheezy", {"Cheeseburger": 6.69, "Fries": 1.00, "Fizzy Drink": 1.00}],
    ["Super", {"Cheeseburger": 6.69, "Large Fries": 2.00, "Smoothie": 2.00}]
]

# Print the Combo menu with format
for combo in menu:
    combo_name = combo[0]
    combo_items = combo[1]
    print(f"Combo Name: {combo_name}")
    for item, price in combo_items.items():
        print(f"\t{item}: {price:.2f}")
