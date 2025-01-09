"""
Author: Namrata Modha
Purpose: Demonstrate Composition in Python
Date: 14-11-2024
"""
# The Book class represents a book with a title and an author.
class Book:
    def __init__(self, title, author):
        # Private attributes for title and author
        self.__title = title  # Title of the book
        self.__author = author  # Author of the book

    # Method to display the book's details
    def show_details(self):
        print(f"Title: {self.__title}") 
        print(f"Author: {self.__author}")

# The Library class represents a library that contains a collection of books.
class Library:
    def __init__(self):
        # A list to store Book objects; this is the composition relationship
        self.books = [] 

    # Method to add a book to the library's collection
    def addBooks(self, book):
        self.books.append(book) 

    # Method to display all the books in the library
    def showBooks(self):
        for book in self.books:
            book.show_details()

# Creating instances of the Book class
bookObj1 = Book("Harry Potter", "J.K Rowling")
bookObj2 = Book("Marvel", "Stan Lee")

# Creating an instance of the Library class
libraryObj = Library()

# Adding books to the library using the addBooks method
libraryObj.addBooks(bookObj1)
libraryObj.addBooks(bookObj2)

# Displaying all the books in the library
libraryObj.showBooks()
