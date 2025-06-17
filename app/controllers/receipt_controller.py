import logging
from flask import Blueprint, request # typo: ignore
from app.services import ReceiptService
from app.mapping import ReceiptMap
from app.mapping import MessageMap
from app.services import MessageBuilder
from app.dto import ReceiptDTO

receipt_bp = Blueprint('receipt', __name__)

@receipt_bp.route('/receipt/<int:id>', methods=['GET'])
def get(id: int):
    receipt = ReceiptService.find(id)
    receipt_schema = ReceiptMap()
    receipt_data = receipt_schema.dump(receipt)
    message_builder = MessageBuilder()
    message_finish = message_builder.add_message('Se encontró el recibo').add_data({'receipt': receipt_data}).build()
    message_map = MessageMap()
    return message_map.dump(message_finish), 200

@receipt_bp.route('/receipts', methods=['GET'])
def get_all():
    receipts = ReceiptService.find_all()
    receipt_schema = ReceiptMap()
    receipts_data = receipt_schema.dump(receipts, many=True)
    message_builder = MessageBuilder()
    message_finish = message_builder.add_message('Se encontraron todos los recibos').add_data({'receipts': receipts_data}).build()
    message_map = MessageMap()
    return message_map.dump(message_finish), 200

@receipt_bp.route('/receipts', methods=['POST'])
def post():
    try:
        receipt_dto_data = request.json
        receipt_dto = ReceiptDTO(**receipt_dto_data)
        
        result_dto = ReceiptService.register_receipt(receipt_dto)
        
        message_builder = MessageBuilder()
        message_finish = message_builder.add_message('Recibo creado exitosamente').add_data({'receipt': result_dto}).build()
        message_map = MessageMap()
        return message_map.dump(message_finish), 201
        
    except Exception as e:
        message_builder = MessageBuilder()
        message_finish = message_builder.add_message(f'Error al crear recibo: {str(e)}').build()
        message_map = MessageMap()
        return message_map.dump(message_finish), 400

@receipt_bp.route('/receipts/<int:id>', methods=['PUT'])
def put(id: int):
    receipt_schema = ReceiptMap()
    new_receipt = receipt_schema.load(request.json)
    new_receipt.id = id
    ReceiptService.update(new_receipt)
    message_map = MessageMap()
    message_builder = MessageBuilder()
    message_finish = message_builder.add_message('Recibo actualizado').build()
    return message_map.dump(message_finish), 200

@receipt_bp.route('/receipts/<int:id>', methods=['DELETE'])
def delete(id: int):
    receipt = ReceiptService.find(id)
    ReceiptService.delete(receipt)
    message_map = MessageMap()
    message_builder = MessageBuilder()
    message_finish = message_builder.add_message(f'Se eliminó el recibo {id}').build()
    return message_map.dump(message_finish), 200
