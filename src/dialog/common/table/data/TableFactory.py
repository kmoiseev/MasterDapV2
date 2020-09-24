import re
from typing import List

from src.dialog.common.table.data.Table import Table
from src.dialog.common.table.data.TableCell import TableCell
from src.dialog.common.table.data.TableHeader import TableHeader
from src.dialog.common.table.data.TableRow import TableRow
from src.storage.common.entity.Entity import Entity
from src.template.table.TableTemplate import TableTemplate
from src.template.table.TableTemplateColumn import TableTemplateColumn
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
            entity.key,
            list(map(
                lambda table_template_column: TableFactory.__create_cell(
                    formatter,
                    table_template_column
                ),
                self.__table_template.columns
            ))
        )

    @staticmethod
    def __create_cell(formatter: StringPropertyFormatter, column_template: TableTemplateColumn):
        formatted_str: str = formatter.format(column_template.value)

        red: bool = False
        if column_template.validation is not None:
            regexp = re.compile(column_template.validation)
            red = not regexp.match(formatted_str)

        return TableCell(
            formatted_str,
            red
        )
