class LibraryItem:
    loan_days = None
    def __init__(self, title):
        self.title = title
        self._is_out = False

    @property
    def is_out(self):
        return self._is_out

    def borrow(self):
        if self.is_out:
            print(f"{self.title}: Cannot borrow — already borrowed.")
            return
        self._is_out = True
        print(f"{self.title}: Borrowed for {self.loan_days} days.")

    def give_back(self):
        if not self.is_out:
            print(f"{self.title}: Cannot return — item was not borrowed.")
            return

        self._is_out = False
        print(f"{self.title}: Returned successfully.")



class Book(LibraryItem):
   loan_days = 14


class Dvd(LibraryItem):
    loan_days = 3


class ReferenceBook(LibraryItem):
    loan_days = 0

    def borrow(self):
        print(f"{self.title}: Cannot borrow — reference books cannot be borrowed.")


items = [
    Book("The Pragmatic Programmer"),
    Dvd("Inception"),
    ReferenceBook("Encyclopedia of Science")
]


for item in items:
    item.borrow()