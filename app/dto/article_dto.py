from dataclasses import dataclass
from typing import Optional

@dataclass
class ArticleDTO:
    id: Optional[int]
    name: str
    description: str
    code_ean13: str
    minimun_stock: float
    id_category: Optional[int] = None
    id_brand: Optional[int] = None