from flask import Flask
from controllers.book_controller import book_bp
from controllers.reader_controller import reader_bp
from controllers.rental_controller import rental_bp

app = Flask(__name__)
app.register_blueprint(book_bp)
app.register_blueprint(reader_bp)
app.register_blueprint(rental_bp)

if __name__ == '__main__':
    app.run(debug=True)
