from models.rental_model import Rental
from uuid import uuid4

rentals = {}

def get_all():
    return [r.to_dict() for r in rentals.values()]

def create(data):
    rental_id = str(uuid4())
    rental = Rental(rental_id, data['reader_id'], data['book_id'], data['days'])
    rentals[rental_id] = rental
    return rental.to_dict()

def update(rental_id, data):
    rental = rentals.get(rental_id)
    if not rental:
        return None
    rental.days = data.get('days', rental.days)
    return rental.to_dict()

def delete(rental_id):
    return rentals.pop(rental_id, None)
