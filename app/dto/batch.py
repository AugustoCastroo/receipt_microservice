from dataclasses import dataclass
from datetime import date

@dataclass(init=True, eq=True)
class Batch():
    """
    Batch con sus atributos
    """
    id: int
    code: str
    expiration_date: date