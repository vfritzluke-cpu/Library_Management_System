class LibraryError(Exception): pass
class BookNotFoundError(LibraryError): pass
class MemberNotFoundError(LibraryError): pass
class BookUnavailableError(LibraryError): pass
class InvalidMenuInputError(LibraryError): pass