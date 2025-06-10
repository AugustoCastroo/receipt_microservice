import os
import requests # app/services/stock.py
from app.dto import Stock
from app.mapping import StockMap, MessageMap, Message
from tenacity import retry, wait_random, stop_after_attempt

class StockService():

    @staticmethod
    @retry(wait=wait_random(min=1, max=3), stop=stop_after_attempt(3))
    def register(stock: Stock) -> 'Message':
        URL_ARTICLE_SERVICE = os.getenv('URL_STOCK_SERVICE')
        if not URL_ARTICLE_SERVICE:
            raise ValueError("Environment variable 'URL_STOCK_SERVICE' is not set.")
        message_map = MessageMap()
        stock_mapping = StockMap()
        stock_json = stock_mapping.dump(stock)
        message_r = requests.post(f"{URL_ARTICLE_SERVICE}/stocks", json=stock_json, verify=False)
        if message_r.status_code == 200:
            return stock_mapping.load(message_r.json())
        else:
            raise Exception(f"Error fetching stock with id {id}: {message_r.status_code} - {message_r.text}")
