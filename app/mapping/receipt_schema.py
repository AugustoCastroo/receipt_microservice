from marshmallow import Schema, fields, post_load # type: ignore
from app.models.receipt import Receipt

class ReceiptMap(Schema):
    id = fields.Integer(dump_only=True)
    id_header = fields.Integer(required=True)
    id_footer = fields.Integer(required=True)
    id_receipt_type = fields.Integer(required=True)

    @post_load
    def make_receipt(self, data, **kwargs):
        return Receipt(**data)
