class Book:
    def __init__(self, book_id, title, author):
        self.id = book_id
        self.title = title
        self.author = author
        self.available = True

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "available": self.available
        }
