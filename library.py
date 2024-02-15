# TO-DO list:
# 1) Create a Library class ✔
# 2) Add the following functionalities:
#       Listing ✔,
#       Adding a book ✔,
#       Removing a book (In progress)

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

    # book_details consists of title, author, release year and number of pages, respectively.
    def add_book(self, book_details):
        self.file.write(f"{book_details[0]},{book_details[1]},{book_details[2]},{book_details[3]}\n")
        print(f"Success - Added the book: {book_details[0]}\n")
