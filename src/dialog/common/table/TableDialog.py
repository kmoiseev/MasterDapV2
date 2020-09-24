from abc import ABCMeta, abstractmethod

from src.dialog.common.Dialog import Dialog
from src.dialog.common.table.TableFuncs import TableFuncs


class TableDialog(Dialog, metaclass=ABCMeta):

    def __init__(self, table_funcs: TableFuncs):
        self.funcs = table_funcs

    @abstractmethod
    def draw_table(self):
        pass
