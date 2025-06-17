from app import db
from app.repositories import ReceiptRepository, ReceiptTypeRepository
from app.dto import ReceiptDTO, StockDTO
from app.models import Receipt, ReceiptItem

class ReceiptService:
   
    @staticmethod
    def save(receipt: Receipt) -> 'Receipt':
        ReceiptRepository.save(receipt)
        return receipt

    @staticmethod
    def find(id: int) -> 'Receipt':
        return ReceiptRepository.find(id)

    @staticmethod
    def find_all() -> list['Receipt']:
        return ReceiptRepository.find_all()

    @staticmethod
    def update(receipt: Receipt) -> 'Receipt':
        return ReceiptRepository.save(receipt)

    @staticmethod
    def delete(receipt: Receipt) -> None:
        ReceiptRepository.delete(receipt)

    @staticmethod
    def register_receipt(receipt_dto: ReceiptDTO) -> 'ReceiptDTO':
        try:
            db.session.begin()
            if not receipt_dto.header:
                raise ValueError("ReceiptDTO.header must be a valid.")
            if not receipt_dto.Footer:
                raise ValueError("ReceiptDTO.Footer must be a valid.")
            
            receipt_type = ReceiptTypeRepository.find(receipt_dto.id_receipt_type)
            if not receipt_type:
                raise ValueError(f"ReceiptType with id {receipt_dto.id_receipt_type} not found")
            
            receipt = Receipt(
                id_header=receipt_dto.header.id,
                id_footer=receipt_dto.Footer.id,
                id_receipt_type=receipt_dto.id_receipt_type
            )

            ReceiptRepository.save(receipt)

            from app.services import ArticleService, StockService
            for item_dto in receipt_dto.items:

                article = ArticleService.find(item_dto.id_article)
                
                receipt_item = ReceiptItem(
                    id_article=item_dto.id_article,
                    quantity=item_dto.quantity,
                    id_batch=item_dto.id_batch,  
                    id_receipt=receipt.id
                )
                db.session.add(receipt_item)
                
                stock_dto = StockDTO(
                    id_article=item_dto.id_article,
                    quantity=item_dto.quantity * receipt_type.type_entry,
                    id_batch=item_dto.id_batch, 
                    id_receipt=receipt.id
                )
                StockService.register(stock_dto)

            db.session.commit()
            return receipt_dto

        except Exception as e:
            db.session.rollback()
            raise ValueError(f"Error registering receipt: {str(e)}")
