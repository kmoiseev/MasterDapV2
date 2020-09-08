from typing import List

from src.dialog.common.table.data.TableHeader import TableHeader
from src.dialog.common.table.data.TableRow import TableRow


class Table:

    def __init__(self, header: TableHeader, rows: List[TableRow]):
        self.header = header
        self.rows = rows
