from abc import abstractmethod

from src.dialog.common.table.data.Table import Table


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
    def get_table_data(self) -> Table:
        pass

    @abstractmethod
    def closed_on_x(self):
        pass
