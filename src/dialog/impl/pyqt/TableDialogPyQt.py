import sys

from PyQt5 import Qt
from PyQt5.QtGui import QPalette, QColor

from abc import ABC

from PyQt5.QtWidgets import QWidget

from src.dialog.common.table.TableDialog import TableDialog
from src.dialog.common.table.TableFuncs import TableFuncs
from src.dialog.common.table.data.Table import Table
from src.template.TemplateManager import TemplateManager
from src.template.table.TableTemplate import TableTemplate


class TableDialogPyQt(TableDialog, ABC):

    def __init__(self, table_funcs: TableFuncs):
        super().__init__(table_funcs)

    def show(self):
        table: Table = self.funcs.get_table_data()

        class ManageDealsWidget(QWidget):

            def __init__(self):
                super().__init__()
                layout = Qt.QVBoxLayout(self)
                labels = list(map(lambda cell: cell.value, table.header.cells))
                table_widget = Qt.QTableWidget(0, len(labels))
                table_widget.setColumnHidden(len(labels), False)
                table_widget.setHorizontalHeaderLabels(labels)
                for k, row in enumerate(table.rows):
                    table_widget.insertRow(table_widget.rowCount())
                    for j, cell in enumerate(row.cells):
                        table_widget.setItem(k, j, Qt.QTableWidgetItem(cell.value))
                        table_widget.item(k, j).setBackground(QColor('red' if cell.red else 'white'))
                table_widget.resizeColumnsToContents()
                table_widget.show()
                layout.addWidget(table_widget)

        app = Qt.QApplication([])
        manage_deals_widget = ManageDealsWidget()
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor('#bdf0d4'))
        manage_deals_widget.setPalette(palette)
        manage_deals_widget.resize(900, 600)
        manage_deals_widget.show()
        app.exec()

    def close(self):
        sys.exit()
