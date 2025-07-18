from app.models.receipt import Receipt
from app.models import ReceiptFooter
from app.repositories.base_repository import CreateAbstractRepository
from app import db


class ReceiptFooterRepository(CreateAbstractRepository):

    @staticmethod
    def save(receipt_footer: ReceiptFooter) -> 'ReceiptFooter':
        db.session.add(receipt_footer)
        db.session.commit()
        return receipt_footer

    @staticmethod
    def get_by_receipt_id(receipt_id: int) -> list[ReceiptFooter]:
        return db.session.query(ReceiptFooter).filter_by(receipt_id=receipt_id).all()
    
    
    
    @staticmethod
    def get_by_id(footer_id: int) -> ReceiptFooter:
        return db.session.query(ReceiptFooter).filter_by(id=footer_id).first()
    
    
  