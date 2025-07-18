from app.models import Receipt
from app.models import ReceiptHeader
from app.repositories.base_repository import CreateAbstractRepository
from app import db



class ReceiptHeaderRepository(CreateAbstractRepository):

    @staticmethod
    def save(receipt_header: ReceiptHeader) -> 'ReceiptHeader':
        db.session.add(receipt_header)
        db.session.commit()
        return receipt_header

    @staticmethod
    def get_by_receipt_id(receipt_id: int) -> list[ReceiptHeader]:
        return db.session.query(ReceiptHeader).filter_by(receipt_id=receipt_id).all()
    
