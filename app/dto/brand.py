from dataclasses import dataclass

@dataclass(init=True, eq=False)
class Brand():
    id: int
    name: str
    description: str
    
    def _eq_(self, brand: object) -> bool:
        return (self.id == brand.id)