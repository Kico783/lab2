from flask import Blueprint, request, jsonify
from services import reader_service

reader_bp = Blueprint('reader_bp', __name__)

@reader_bp.route('/readers', methods=['GET'])
def get_all_readers():
    return jsonify(reader_service.get_all())

@reader_bp.route('/readers', methods=['POST'])
def create_reader():
    return jsonify(reader_service.create(request.json)), 201

@reader_bp.route('/readers/<reader_id>', methods=['PUT'])
def update_reader(reader_id):
    result = reader_service.update(reader_id, request.json)
    if result:
        return jsonify(result)
    return jsonify({'error': 'Reader not found'}), 404

@reader_bp.route('/readers/<reader_id>', methods=['DELETE'])
def delete_reader(reader_id):
    if reader_service.delete(reader_id):
        return '', 204
    return jsonify({'error': 'Reader not found'}), 404
