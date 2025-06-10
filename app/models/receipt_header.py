from dataclasses import dataclass
from datetime import datetime


@dataclass(init=True, eq=True)
class ReceiptHeader():

    id: int
    submission_date: datetime

    