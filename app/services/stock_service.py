import os
import requests # app/services/stock.py
from app.dto import Stock
from app.mapping import StockMap

class StockService():

    @staticmethod
    def find(id: int) -> 'Stock':
        URL_ARTICLE_SERVICE = os.getenv('URL_ARTICLE_SERVICE')
        if not URL_ARTICLE_SERVICE:
            raise ValueError("Environment variable 'URL_ARTICLE_SERVICE' is not set.")
        stock_mapping = StockMap()
        sotck_r = stock_mapping.load(requests.get(f"{URL_ARTICLE_SERVICE}/stock{id}", verify=False))
        if stock_r.status_code == 200:
            return stock_mapping.load(stock_r.json())
        else:
            raise Exception(f"Error fetching stock with id {id}: {stock_r.status_code} - {stock_r.text}")
