from abc import ABC
from tkinter import Tk

from src.dialog.common.table.TableDialog import TableDialog
from src.dialog.common.table.TableFuncs import TableFuncs


class TableDialogTk(TableDialog, ABC):

    def __init__(self, table_funcs: TableFuncs):
        super().__init__(table_funcs)

        self.root = Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.funcs.closed_on_x)

    def show(self):
        self.funcs.get_table_data()

    def close(self):
        self.root.destroy()
