from typing import List

from src.dialog.common.table.data.TableCell import TableCell


class TableRow:

    def __init__(self, entity_key: str, cells: List[TableCell]):
        self.entity_key = entity_key
        self.cells = cells
