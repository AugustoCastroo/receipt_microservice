from app.models import Article
from typing import List
import requests # app/services/article_service.py


class ArticleService():
    
    @staticmethod
    def find(id: int) -> 'Article':
        article_service = ArticleRepository.find(id)
        if not article_service:
                    raise ValueError(f"Article with ID {id} not found.")
        return article_service
    
    @staticmethod
    def find_by(**kwargs) -> List['Article']:
        return ArticleRepository.find_by(**kwargs)
