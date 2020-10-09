from abc import abstractmethod

from src.dialog.common.table.data.Table import Table


class TableFuncs:

    @abstractmethod
    def form_doc(self, key: str):
        pass

    @abstractmethod
    def create_entity(self):
        pass

    @abstractmethod
    def edit_entity(self, key: str):
        pass

    @abstractmethod
    def delete_entity(self, key):
        pass

    @abstractmethod
    def duplicate_entity(self, key):
        pass

    @abstractmethod
    def get_table_data(self) -> Table:
        pass
