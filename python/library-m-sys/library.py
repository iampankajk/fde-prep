from models import Book, Member

class Library:
    def __init__(self):
        self.books = []
        self.members = []


    def add_book(self):
        isbn = input("ISBN: ")
        title = input("Title: ")
        author = input("Author: ")
        genre = input("Genre: ")
        book  = Book(isbn, title, author, genre)
        self.books.append(book)

    def borrow_book(self):
        ...

    def register_member(self):
        name = input("Name: ")
        type = input("Member Type: ")
        id  = len(self.members) + 1
        new_member = Member(name, id, type)
        self.members.append(new_member)

    def return_book(self):
        ...

    def search_book(self, text):
        ...
        
