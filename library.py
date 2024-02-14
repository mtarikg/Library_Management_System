# TO-DO list:
# 1) Create a Library class ✔
# 2) Add the following functionalities:
#       Listing ✔,
#       Adding a book,
#       Removing a book

class Library:
    def __init__(self, file_name):
        self.file = open(file_name, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        books = self.file.read().splitlines()
        for book in books:
            data = book.split(",")
            title = data[0]
            author = data[1]
            print(f"Title: {title} Author: {author}")
