from app.models import Stock, ReceiptItem, Article
from app.repositories import ReceiptRepository
from app.services import ArticleService
from app.services import BrandService


class StockService():

    @staticmethod
    def register(stock: Stock) -> Stock:
        article = ArticleService.find(stock.article.id)
        if not article:
            raise ValueError(f"Article with ID {stock.article.id} does not exist.")

        receipt = ReceiptRepository.find(stock.receipt.id)
        if not receipt:
            raise ValueError(f"Receipt with ID {stock.receipt.id} does not exist.")

        brand = BrandService.find(article.brand_id)
        if not brand:
            raise ValueError(f"Brand with ID {article.brand_id} does not exist.")
        return ArticleService.save(stock)
