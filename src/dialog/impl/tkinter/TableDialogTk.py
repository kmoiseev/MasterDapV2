from abc import ABC

from src.dialog.common.table.TableDialog import TableDialog


class TableDialogTk(TableDialog, ABC):
    def draw(self):
        pass

    def close(self):
        pass
