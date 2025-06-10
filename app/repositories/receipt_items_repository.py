from app.models import ReceiptItem
from app.repositories import CreateAbstractRepository
from app import db


class ReceiptItemsRepository(CreateAbstractRepository):

    @staticmethod
    def save(receipt_item: ReceiptItem) -> 'ReceiptItem':
        db.session.add(receipt_item)
        db.session.commit()
        return receipt_item

    @staticmethod
    def get_by_receipt_id(receipt_id: int) -> list[ReceiptItem]:
        return db.session.query(ReceiptItem).filter_by(receipt_id=receipt_id).all()
    
    