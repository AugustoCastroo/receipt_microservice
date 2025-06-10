from dataclasses import dataclass


@dataclass(init=True, eq=True)
class Receipt():
 
    id: int
    id_header: int 
    id_footer: int 
    items = 'ReceiptItem'
    id_receipt_type: int
    receipt_type = 'ReceiptType'
    
    
    
   