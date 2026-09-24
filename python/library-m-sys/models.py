class Member:
    max_books = 2
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_isbns = []

    def can_borrow(self):
        return len(self.borrowed_isbns) < self.max_books

    ...

class RegularMember(Member):
    max_books = 2


class PremiumMember(Member):
    max_books = 5

class Book:
    def __init__(self, isbn, title, author, genre, copies=1):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.genre = genre
        self.copies = copies
