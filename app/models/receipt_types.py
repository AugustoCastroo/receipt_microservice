from dataclasses import dataclass


@dataclass(init=True, eq=True)
class ReceiptType():

    id: int
    name: str 
    description: str 
    type_entry: int 
