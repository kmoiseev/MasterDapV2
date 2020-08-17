from abc import ABCMeta

from src.dialog.common.Dialog import Dialog
from src.dialog.common.table.TableFuncs import TableFuncs


class TableDialog(Dialog, metaclass=ABCMeta):

    def __init__(self, table_funcs: TableFuncs):
        self.funcs = table_funcs
