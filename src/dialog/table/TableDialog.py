from abc import ABCMeta

from src.dialog.Dialog import Dialog
from src.dialog.table.TableFuncs import TableFuncs


class TableDialog(Dialog, metaclass=ABCMeta):

    def __init__(self, table_funcs: TableFuncs):
        self.__funcs = table_funcs