from app.models import Article
from typing import List
import requests # app/services/article.py
from app.mapping.article_schema import ArticleMap
from app import cache
from tenacity import retry, wait_random, stop_after_attempt
import os



class ArticleService():

    @staticmethod
    @retry(wait=wait_random(min=1, max=3), stop=stop_after_attempt(3))
    def find(id: int) -> 'Article':
        URL_ARTICLE_SERVICE = os.getenv('URL_ARTICLE_SERVICE')
        if not URL_ARTICLE_SERVICE:
            raise ValueError("Environment variable 'URL_ARTICLE_SERVICE' is not set.")
        result = cache.get(f'articles_{id}')
        if result is None:  
            article_mapping = ArticleMap()
            article_r = article_mapping.load(requests.get(f"{URL_ARTICLE_SERVICE}/articles/{id}", verify=False))
            if article_r.status_code == 200:
                result = article_mapping.load(article_r.json())
                cache.set(f'articles_{id}', result, timeout=15)   
            else:
                raise Exception(f"Error fetching article with id {id}: {article_r.status_code} - {article_r.text}")
            return result