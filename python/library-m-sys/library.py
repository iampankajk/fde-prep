from models import Book, Member
from Error import LibraryError, BookNotFoundError, BookNotAvailableError, MemberNotFoundError, BorrowLimitReachedError
import json
import os

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}
        self.genres = set()


    def add_book(self, isbn, title, author, genre, copies = 1):
        if isbn in self.books:
            self.books[isbn].copies += copies
            self.books[isbn].available_copies +=copies
        else:
            self.books[isbn] = Book(isbn, title, author, genre, copies)
        self.genres.add(genre)


    def find_book(self,isbn):
        if isbn not in self.books:
            raise BookNotFoundError(f"No book with ISBN {isbn}.")
        return self.books[isbn]

    def search_books(self, keyword):
        keyword = keyword.lower()
        results = []
        for book in self.books.values():
            if keyword in book.title.lower() or keyword in book.author.lower():
                results.append(book)
        return results

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

