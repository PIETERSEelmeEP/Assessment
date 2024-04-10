import easygui

# Get the input as a string
input_str = easygui.enterbox("Enter ID:", title="Contact ID")

# Convert the input to a float with two decimal places
try:
    contact_ID = "{:.2f}".format(float(input_str))
    easygui.msgbox(f"Contact ID: {contact_ID}")
except ValueError:
    easygui.msgbox("Invalid input! Please enter a valid number.")
