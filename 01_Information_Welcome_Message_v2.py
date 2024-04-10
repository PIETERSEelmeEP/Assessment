"""Puts 01_Information_Welcome_Message_v1 into a function
"""
import easygui


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


# Main Routine
welcome_selected_action()
