import sys
from library import Library


def main():
    print("Welcome to our Library Management System!\n")

    while True:
        display_menu()  # Displays all options available in the system
        try:
            menu_item = int(input("Please select an option above: "))
            lib = Library("books.txt")
            # Directs to a subpage based on the user input
            menu_director(menu_item, lib)
        except ValueError:
            print("Please type only numbers.\n")


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
        book_inputs = add_book_inputs()
        obj.add_book(book_inputs)
    elif menu_item == 3:
        book_title = input("Title of the book to be removed: ")
        obj.remove_book(book_title)
    elif menu_item == 4:
        print("Thanks for using our system!")
        print("Quitting...")
        sys.exit(0)
    else:
        print("Invalid input. Please try again.\n")


def add_book_inputs():
    inputs = []
    title = input("Book Title: ")
    author = input("Book Author: ")
    release_year = input("Release Year: ")
    # To not abort the process abruptly, going back to the main menu,
    # it keeps asking the user to enter a correct type of value.
    while release_year.isnumeric() != True:
        print("Release year can only be an integer.")
        release_year = input("Release Year: ")
    page_number = input("Page number: ")
    while page_number.isnumeric() != True:
        print("Number of pages can only be an integer.")
        page_number = input("Page number: ")
    inputs.extend([title, author, release_year, page_number])
    return inputs


main()
