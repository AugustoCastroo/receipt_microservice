from dataclasses import dataclass

@dataclass(init=True, eq=True)
class Category:
    id: int
    name: str
    description: str