from marshmallow import Schema, fields, post_load
from app.dto import StockDTO

class StockMap(Schema):
    id = fields.Integer(dump_only=True)
    id_article = fields.Integer(required=True)
    id_receipt = fields.Integer(required=True)
    quantity = fields.Integer(required=True)
    id_batch = fields.Integer(required=True)

    @post_load
    def bind_stock(self, data, **kwargs):
        return StockDTO(**data)