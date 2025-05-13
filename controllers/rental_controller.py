from flask import Blueprint, request, jsonify
from services import rental_service

rental_bp = Blueprint('rental_bp', __name__)

@rental_bp.route('/rentals', methods=['GET'])
def get_all_rentals():
    return jsonify(rental_service.get_all())

@rental_bp.route('/rentals', methods=['POST'])
def create_rental():
    return jsonify(rental_service.create(request.json)), 201

@rental_bp.route('/rentals/<rental_id>', methods=['PUT'])
def update_rental(rental_id):
    result = rental_service.update(rental_id, request.json)
    if result:
        return jsonify(result)
    return jsonify({'error': 'Rental not found'}), 404

@rental_bp.route('/rentals/<rental_id>', methods=['DELETE'])
def delete_rental(rental_id):
    if rental_service.delete(rental_id):
        return '', 204
    return jsonify({'error': 'Rental not found'}), 404
