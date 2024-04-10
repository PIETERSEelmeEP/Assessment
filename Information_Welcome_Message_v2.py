"""Puts Information&Welcome_Message_v1 into a function
"""
import easygui


def welcome_selected_action():
    easygui.msgbox("Welcome", title="Welcome Message")
    easygui.buttonbox("Please select action for the Combo Menu:",
                      title="Select Action", choices=["Add", "Search",
                                                      "Delete",
                                                      "Print Full Menu",
                                                      "Exit Program"])


welcome_selected_action()
