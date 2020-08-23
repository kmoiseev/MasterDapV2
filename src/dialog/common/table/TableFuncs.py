from abc import abstractmethod
from typing import List

from src.dialog.common.table.data.Table import Table
from src.storage.common.entity.Entity import Entity


class TableFuncs:
    def __init__(self):
        self.closed_on_x = None

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
    def get_table_data(self) -> Table:
        pass
