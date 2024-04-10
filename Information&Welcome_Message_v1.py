"""Create an easygui message box welcoming the user then a new easygui
buttonbox should appear and ask if they want to 'Add', 'Search', 'Delete',
'Print Full Menu', or 'Exit Program'
"""
import easygui

easygui.msgbox("Welcome", title="Welcome Message")
easygui.buttonbox("Please select action for the Combo Menu:",
                  title="Select Action", choices=["Add", "Search", "Delete",
                                                  "Print Full Menu",
                                                  "Exit Program"])
