import sys
from library import Library


def main():
    print("Welcome to our Library Management System!\n")

    while True:
        display_menu()  # Displays all options available in the system
        try:
            menu_item = int(input("Please select an option below: "))
            lib = Library("books.txt")
            # Directs to a subpage based on the user input
            menu_director(menu_item, lib)
        except ValueError:
            print("Please type only numbers.")


def display_menu():
    print("*** MENU ***")
    print("1) List Books")
    print("2) Add a Book")
    print("3) Remove a Book")
    print("4) Quit\n")


def menu_director(menu_item: int, obj: Library):
    if menu_item == 1:
        obj.list_books()
    elif menu_item == 2:
        print("Directing the user to Add a Book menu...")
    elif menu_item == 3:
        print("Asking the user a title to remove a book...")
    elif menu_item == 4:
        print("Thanks for using our system!")
        print("Quitting...")
        sys.exit(0)
    else:
        print("Invalid input. Please try again.\n")


main()
