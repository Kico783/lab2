from models.reader_model import Reader
from uuid import uuid4

readers = {}

def get_all():
    return [r.to_dict() for r in readers.values()]

def create(data):
    reader_id = str(uuid4())
    reader = Reader(reader_id, data['name'], data['email'])
    readers[reader_id] = reader
    return reader.to_dict()

def update(reader_id, data):
    reader = readers.get(reader_id)
    if not reader:
        return None
    reader.name = data.get('name', reader.name)
    reader.email = data.get('email', reader.email)
    return reader.to_dict()

def delete(reader_id):
    return readers.pop(reader_id, None)
