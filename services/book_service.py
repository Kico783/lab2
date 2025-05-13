from models.book_model import Book
from uuid import uuid4

books = {}

def get_all():
    return [b.to_dict() for b in books.values()]

def create(data):
    book_id = str(uuid4())
    book = Book(book_id, data['title'], data['author'])
    books[book_id] = book
    return book.to_dict()

def update(book_id, data):
    book = books.get(book_id)
    if not book:
        return None
    book.title = data.get('title', book.title)
    book.author = data.get('author', book.author)
    book.available = data.get('available', book.available)
    return book.to_dict()

def delete(book_id):
    return books.pop(book_id, None)
