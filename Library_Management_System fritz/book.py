class Book:
    def __init__(self, book_id: str, title: str, author: str):
        self._book_id = book_id
        self._title = title
        self._author = author
        self._available = True