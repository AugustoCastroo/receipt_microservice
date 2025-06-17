from dataclasses import dataclass
from datetime import date
from typing import Optional

@dataclass
class BatchDTO:
    id: Optional[int]
    code: str
    expiration_date: date