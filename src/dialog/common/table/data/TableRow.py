from typing import List

from src.dialog.common.table.data.TableCell import TableCell


class TableRow:

    def __init__(self, cells: List[TableCell]):
        self.cells = cells
