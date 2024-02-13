import sys

def main():
    menu_item = 0 # Initializing to 0 results in executing the while loop at least once, mimicking a do-while loop.

    while menu_item < 1 or menu_item > 4:
        display_menu() # Displays all options available in the system
        try:
            menu_item = int(input("Please select an option below: "))
        except ValueError:
            print("Please type only numbers.")

        menu_director(menu_item) # Directs to a subpage based on the user input

def display_menu():
    print("Welcome to our Library Management System!")
    print("")
    print("*** MENU ***")
    print("1) List Books")
    print("2) Add a Book")
    print("3) Remove a Book")
    print("4) Quit")
    print("")

def menu_director(menu_item):
    if menu_item == 1:
        print("Listing books...")
    elif menu_item == 2:
        print("Directing the user to Add a Book menu...")
    elif menu_item == 3:
        print("Asking the user a title to remove a book...")
    elif menu_item == 4:
        print("Thanks for using our system!")
        print("Quitting...")
        sys.exit(0)
    else:
        print("Invalid input. Please try again.")
        print("")

main()