from flask import Blueprint, request, jsonify
from services import book_service

book_bp = Blueprint('book_bp', __name__)

@book_bp.route('/books', methods=['GET'])
def get_all_books():
    return jsonify(book_service.get_all())

@book_bp.route('/books', methods=['POST'])
def create_book():
    return jsonify(book_service.create(request.json)), 201

@book_bp.route('/books/<book_id>', methods=['PUT'])
def update_book(book_id):
    result = book_service.update(book_id, request.json)
    if result:
        return jsonify(result)
    return jsonify({'error': 'Book not found'}), 404

@book_bp.route('/books/<book_id>', methods=['DELETE'])
def delete_book(book_id):
    if book_service.delete(book_id):
        return '', 204
    return jsonify({'error': 'Book not found'}), 404
