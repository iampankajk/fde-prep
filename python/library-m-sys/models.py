class Book:
    def __init__(self, isbn, title, author, genre, copies=1):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.genre = genre
        self.copies = copies
        self.available_copies = copies

    def __str__(self):
        status = f"{self.available_copies}/{self.copies} available"
        return f"[{self.isbn}] {self.title} by {self.author} ({self.genre}) - {status}"

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, data):
        book = cls(data["isbn"], data["title"], data["author"], data["genre"], data["copies"])
        book.available_copies = data["available_copies"]
        return book


class Member:
    max_books = 2
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_isbns = []

    def can_borrow(self):
        return len(self.borrowed_isbns) < self.max_books

    def to_dict(self):
        return {
            "type": self.__class__.__name__,
            "member_id": self.member_id,
            "name": self.name,
            "borrowed_isbns": self.borrowed_isbns,
        }

    def __str__(self):
        return f"{self.name} ({self.__class__.__name__}) - {len(self.borrowed_isbns)}/{self.max_books} books"
    

class RegularMember(Member):
    max_books = 2


class PremiumMember(Member):
    max_books = 5


MEMBER_TYPES = {"RegularMember": RegularMember, "PremiumMember": PremiumMember}