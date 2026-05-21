from book import Book
from member import Member

class Loan:
    def __init__(self, loan_id: str, book: Book, member: Member):
        self._loan_id = loan_id
        self._book = book
        self._member = member
        self._is_active = True