class Reader:
    def __init__(self, reader_id, name, email):
        self.id = reader_id
        self.name = name
        self.email = email

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }
