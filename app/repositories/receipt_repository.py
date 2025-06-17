from typing import List
from app.models.receipt import Receipt
from app.repositories.base_repository import CreateAbstractRepository, ReadAbstractRepository
from app import db

class ReceiptRepository(CreateAbstractRepository, ReadAbstractRepository):

    @staticmethod
    def save(receipt: Receipt) -> 'Receipt' :
        db.session.add(receipt)
        db.session.commit()
        return receipt
    
    @staticmethod
    def find(id: int) -> 'Receipt':
        return Receipt.query.get(id)

    @staticmethod
    def find_all() -> List['Receipt']:
        return Receipt.query.all()
    
    @staticmethod
    def find_by(**kwargs) -> List[Receipt]:
        return Receipt.query.filter_by(**kwargs).all()