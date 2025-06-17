from dataclasses import dataclass
from typing import Optional

@dataclass
class StockDTO:
    id_article: int
    quantity: int
    id_batch: int
    id_receipt: int
    id: Optional[int] = None