from app import db  
from app.models import Receipt
from app.repositories import ReceiptRepository, ReceiptTypeRepository
from app.dto import ReceiptDTO
from app.models import ReceiptItem, Stock   

class ReceiptService:
   
    @staticmethod
    def save(receipt: Receipt) -> 'Receipt':

        ReceiptRepository.save(receipt)
        return receipt

    @staticmethod
    def register_receipt(receipt_dto: ReceiptDTO) -> 'ReceiptDTO':
  
        try:
            db.session.begin()
            if not receipt_dto.header:
                raise ValueError("ReceiptDTO.header must be a valid.")
            if not receipt_dto.Footer:
                raise ValueError("ReceiptDTO.Footer must be a valid.")
            
            receipt_type = ReceiptTypeRepository.exists(receipt_dto.id_receipt_type)          
            receipt = Receipt(
                id_header=receipt_dto.header.id,
                id_footer=receipt_dto.footer.id,
                id_receipt_type=receipt_dto.id_receipt_type
            )

            ReceiptRepository.save(receipt)

            from app.services import ArticleService, StockService, BatchService
            for item_dto in receipt_dto.items:
            
                article = ArticleService.find(item_dto.id_article)
                batch = BatchService.find(item_dto.id_batch)
                receipt_item = ReceiptItem(
                    article=article,
                    quantity=item_dto.quantity,
                    batch=batch,
                    receipt=receipt
                )
                db.session.add(receipt_item)
                stock = Stock(article=article,
                    quantity=item_dto.quantity * receipt_type.type_entry,
                    batch=batch,
                    receipt=receipt)
                StockService.register(stock)

            db.session.commit()

            return receipt_dto

        except Exception as e:
            db.session.rollback()
            raise ValueError(f"Error registering receipt: {str(e)}")
