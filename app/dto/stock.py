from dataclasses import dataclass

@dataclass(init=True, eq=True)
class Stock():
    id: int
    id_article: int
    id_receipt: int
    quantity: int
    id_batch: int
    article: 'Article'
    batch: 'Batch'
    receipt: 'Receipt'