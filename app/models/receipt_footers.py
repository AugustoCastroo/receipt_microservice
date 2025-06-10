from dataclasses import dataclass


@dataclass(init=True, eq=True)
class ReceiptFooter():
    
    id: int 
    total: float

