from app.dto import BatchDTO
from app.repositories import BatchRepository
from typing import List

class BatchService():
    
    @staticmethod
    def save(batch: BatchDTO) -> 'BatchDTO':
        BatchRepository.save(batch)
        return batch

    @staticmethod
    def delete(batch: 'BatchDTO') -> None:
        BatchRepository.delete(batch)

    @staticmethod
    def find(id: int) -> 'BatchDTO':
        return BatchRepository.find(id)

    @staticmethod
    def find_all() -> List['BatchDTO']:
        return BatchRepository.find_all()

    @staticmethod
    def find_by(**kwargs) -> List['BatchDTO']:
        return BatchRepository.find_by(**kwargs)

    @staticmethod
    def update(batch: 'BatchDTO') -> 'BatchDTO':
        BatchRepository.update(batch)
        return batch