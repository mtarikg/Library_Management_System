# TO-DO list:
# 1) Create a Library class ✔
# 2) Add the following functionalities:
#       Listing ✔,
#       Adding a book ✔,
#       Removing a book ✔

class Library:
    def __init__(self, file_name):
        self.file = open(file_name, "a+")

    def __del__(self):
        self.file.close()

    """ 
    Potential bugs:
        In case the user enters a title including a comma,
        it'll break down the applied logic: splitting items by a comma.
    """
    def list_books(self):
        self.file.seek(0)
        books = self.file.read().splitlines()
        for book in books:
            data = book.split(",")
            title = data[0]
            author = data[1]
            print(f"Title: {title} - Author: {author}")
        print("")

    """
    Complexity Analysis:
        The running time of adding a book is Θ(1),
        since it adds each book at the end of the list.
    Possible Improvements:
        1- Assigning an ID to each book added to the system
        2- Checking whether there is already an existing record by a method, e.g., is_book_existing
        3- If exists, a prompt to the user of whether they would want to update the book or not,
            directing the user to another interface, e.g., edit_book.
    """
    # book_details consists of title, author, release year and number of pages, respectively.
    def add_book(self, book_details):
        self.file.write(f"{book_details[0]},{book_details[1]},{book_details[2]},{book_details[3]}\n")
        print(f"Success - Added the book: {book_details[0]}\n")

    """
    Complexity Analysis:
        The upper bound of removing a book is O(N),
        whereas the lower bound is Ω(1).
    """
    def remove_book(self, book_title):
        self.file.seek(0)
        books = self.file.read().splitlines()
        for book in books:
            title = book.split(",", 1)[0] # 1 specifies to split only the title column
            if book_title == title:
                books.remove(book)
                print(f"Success - Removed the book: {book_title}\n")
                break
        self.file.truncate(0)
        for book in books:
            self.file.write(f"{book}\n")

