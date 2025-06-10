from dataclasses import dataclass


@dataclass(init=True, eq=False)
class ArticleDTO():
    """
    Article con sus atributos
    """
    id: int
    name: str
    description: str
    id_category: int
    id_brand: int
    minimun_stock: int
    code_ean13: str
    brand: 'Brand'
    category: 'Category'

    def _eq_(self, article:object) -> bool:
        return self.name == article.name and self.code_ean13 == article.code_ean13