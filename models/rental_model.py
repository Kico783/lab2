class Rental:
    def __init__(self, rental_id, reader_id, book_id, days):
        self.id = rental_id
        self.reader_id = reader_id
        self.book_id = book_id
        self.days = days

    def to_dict(self):
        return {
            "id": self.id,
            "reader_id": self.reader_id,
            "book_id": self.book_id,
            "days": self.days
        }
