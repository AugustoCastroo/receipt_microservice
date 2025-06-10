from dataclasses import dataclass


@dataclass(init=True, eq=True)
class ReceiptItem():

    id: int 
    id_article: int 
    quantity: int 
    id_batch: int 
    id_receipt: int 
    receipt = 'Receipt'
    article = 'Article'
    batch = 'Batch'