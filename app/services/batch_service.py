import os
import requests
from app.dto import Batch
from app.mapping import BatchMap

class BatchService():

    @staticmethod
    def find(id: int) -> 'Batch':
        URL_ARTICLE_SERVICE = os.getenv('URL_ARTICLE_SERVICE')
        if not URL_ARTICLE_SERVICE:
            raise ValueError("Environment variable 'URL_ARTICLE_SERVICE' is not set.")
        batch_mapping = BatchMap()
        batch_r = batch_mapping.load(requests.get(f"{URL_ARTICLE_SERVICE}/batch/{id}", verify=False))
        if batch_r.status_code == 200:
            return batch_mapping.load(batch_r.json())
        else:
            raise Exception(f"Error fetching batch with id {id}: {batch_r.status_code} - {batch_r.text}")