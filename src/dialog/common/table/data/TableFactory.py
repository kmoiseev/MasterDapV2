from typing import List

from src.dialog.common.table.data.Table import Table
from src.dialog.common.table.data.TableCell import TableCell
from src.dialog.common.table.data.TableHeader import TableHeader
from src.storage.common.entity.Entity import Entity
from src.template.table.TableTemplate import TableTemplate


class TableFactory:

    def __init__(self, table_template: TableTemplate):
        self.table_template = table_template

    def create(self, entities: List[Entity]) -> Table:
        header: TableHeader = TableHeader(
            list(map(
                lambda table_template_column: TableCell(table_template_column.header),
                self.table_template.columns
            ))
        )
        # rows: TableRow =
        return Table(header, [])