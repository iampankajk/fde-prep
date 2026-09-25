class LibraryError(Exception):
    """Base class for all library-related errors."""
    pass
 
 
class BookNotFoundError(LibraryError):
    pass
 
 
class BookNotAvailableError(LibraryError):
    pass
 
 
class MemberNotFoundError(LibraryError):
    pass
 
 
class BorrowLimitReachedError(LibraryError):
    pass