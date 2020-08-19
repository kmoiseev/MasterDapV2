from typing import List

from src.dialog.common.table.data.TableCell import TableCell


class TableHeader:

    def __init__(self, cells: List[TableCell]):
        self.cells = cells
