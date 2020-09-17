from src.template.table.TableTemplateColumn import TableTemplateColumn


class TableTemplate:

    def __init__(self, table_template_json):
        self.columns = list(map(
            lambda column: TableTemplateColumn(column['header'], column["value"], column.get("validation", None)),
            table_template_json["columns"]
        ))
