from app.models import ReceiptItem
from app.repositories import ReceiptItemsRepository
from app.models import ReceiptType


class ReceiptItemsService:

    @staticmethod
    def get_all_receipt_items(ReceiptType: ReceiptType) -> list[ReceiptType]:
  
        return ReceiptItemsRepository.get_all_receipt_items(ReceiptType)

    @staticmethod
    def get_receipt_item_by_id(receipt_item_id: int) -> 'ReceiptType':

        return ReceiptItemsRepository.get_receipt_item_by_id(receipt_item_id)

    @staticmethod
    def create_receipt_item(receipt_item_data: dict) -> 'ReceiptType':

        return ReceiptItemsRepository.create_receipt_item(receipt_item_data)

    @staticmethod
    def update_receipt_item(receipt_item_id: int, updated_data: dict) -> 'ReceiptType':

        return ReceiptItemsRepository.update_receipt_item(receipt_item_id, updated_data)

    @staticmethod
    def delete_receipt_item(receipt_item_id: int) -> None:

        return ReceiptItemsRepository.delete_receipt_item(receipt_item_id)