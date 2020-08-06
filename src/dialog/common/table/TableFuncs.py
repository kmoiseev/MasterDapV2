from abc import abstractmethod
from typing import List

from src.storage.entity.Entity import Entity


class TableFuncs:
    @abstractmethod
    def form_doc(self, key: str):
        pass

    @abstractmethod
    def create_deal(self):
        pass

    @abstractmethod
    def edit_deal(self, key: str):
        pass

    @abstractmethod
    def delete_deal(self, key):
        pass

    @abstractmethod
    def get_table_data(self) -> List[Entity]:
        pass