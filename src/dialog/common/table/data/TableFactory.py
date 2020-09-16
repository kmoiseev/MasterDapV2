from typing import List

from src.dialog.common.table.data.Table import Table
from src.dialog.common.table.data.TableCell import TableCell
from src.dialog.common.table.data.TableHeader import TableHeader
from src.dialog.common.table.data.TableRow import TableRow
from src.storage.common.entity.Entity import Entity
from src.template.table.TableTemplate import TableTemplate
from src.util.props.StringPropertyFormatter import StringPropertyFormatter


class TableFactory:

    def __init__(self, table_template: TableTemplate):
        self.__table_template = table_template

    def create(self, entities: List[Entity]) -> Table:
        header: TableHeader = TableHeader(
            list(map(
                lambda table_template_column: TableCell(table_template_column.header),
                self.__table_template.columns
            ))
        )
        rows: List[TableRow] = list(map(
            self.__entity_to_table_row,
            entities
        ))
        return Table(header, rows)

    def __entity_to_table_row(self, entity: Entity) -> TableRow:
        formatter: StringPropertyFormatter = StringPropertyFormatter(entity.props)
        return TableRow(
            list(map(
                lambda table_template_column: TableCell(
                    formatter.format(table_template_column.value)
                ),
                self.__table_template.columns
            ))
        )