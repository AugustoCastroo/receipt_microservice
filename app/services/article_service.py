from app.models import Article
from typing import List
import requests # app/services/article.py
from app.mapping.article_schema import ArticleMap
import os



class ArticleService():

    @staticmethod
    def find(id: int) -> 'Article':
        URL_ARTICLE_SERVICE = os.getenv('URL_ARTICLE_SERVICE')
        if not URL_ARTICLE_SERVICE:
            raise ValueError("Environment variable 'URL_ARTICLE_SERVICE' is not set.")
        article_mapping = ArticleMap()
        article_r = article_mapping.load(requests.get(f"{URL_ARTICLE_SERVICE}/articles/{id}", verify=False))
        if article_r.status_code == 200:
            return article_mapping.load(article_r.json())
        else:
            raise Exception(f"Error fetching article with id {id}: {article_r.status_code} - {article_r.text}")