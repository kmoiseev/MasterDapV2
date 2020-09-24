import sys
from abc import ABC

from PyQt5 import Qt
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QWidget

from src.dialog.common.table.TableDialog import TableDialog
from src.dialog.common.table.TableFuncs import TableFuncs
from src.dialog.common.table.data.Table import Table
from src.dialog.impl.pyqt.ButtonUtils import create_qt_button
from src.storage.Icons import *


class TableDialogPyQt(TableDialog, ABC):

    def __init__(self, table_funcs: TableFuncs):
        super().__init__(table_funcs)
        self.dialog_widget = None
        self.table_widget = None

    def show(self):
        app = Qt.QApplication([])

        self.dialog_widget = self.make_dialog_widget()

        layout = Qt.QVBoxLayout(self.dialog_widget)
        layout.addWidget(self.make_create_entity_button())

        self.table_widget = self.make_table_widget()
        layout.addWidget(self.table_widget)

        self.draw_table()

        self.dialog_widget.show()

        app.exec()

    def make_create_entity_button(self):
        create_entity_button = create_qt_button(Qt.QIcon(CREATE), self.funcs.create_entity, "Создать ДАП")
        create_entity_button.setFixedWidth(110)
        create_entity_button.setFixedHeight(30)
        return create_entity_button

    @staticmethod
    def make_dialog_widget():
        dialog_widget = QWidget()
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor('#bdf0d4'))
        dialog_widget.setPalette(palette)
        dialog_widget.resize(900, 600)
        return dialog_widget

    def make_table_widget(self) -> Qt.QTableWidget:
        table: Table = self.funcs.get_table_data()
        return Qt.QTableWidget(0, len(table.header.cells))

    def draw_table(self):
        table_widget = self.table_widget
        table = self.funcs.get_table_data()

        table_widget.setRowCount(0)
        labels = list(map(lambda x: x.value, table.header.cells))
        table_widget.setColumnHidden(len(labels), False)
        table_widget.setHorizontalHeaderLabels(labels)
        for k, row in enumerate(table.rows):
            table_widget.insertRow(table_widget.rowCount())
            for j, cell in enumerate(row.cells):
                table_widget.setItem(k, j, Qt.QTableWidgetItem(cell.value))
                create_deal_button = create_qt_button(
                    Qt.QIcon(FORM),
                    lambda: self.funcs.form_doc(row.entity_key),
                    "Сформировать"
                )
                edit_deal_button = create_qt_button(
                    Qt.QIcon(EDIT),
                    lambda: self.funcs.edit_entity(row.entity_key)
                )
                delete_deal_button = create_qt_button(
                    Qt.QIcon(DELETE),
                    lambda: self.funcs.delete_entity(row.entity_key)
                )
                table_widget.setCellWidget(j, 0, create_deal_button)
                table_widget.setCellWidget(j, 1, edit_deal_button)
                table_widget.setCellWidget(j, 2, delete_deal_button)
                if j == 7 or j == 8:  # Костыль какой то
                    table_widget.item(k, j).setBackground(QColor('orange' if cell.red else 'green'))
        table_widget.resizeColumnsToContents()

    def enable(self):
        self.dialog_widget.setDisabled(False)

    def disable(self):
        self.dialog_widget.setDisabled(True)

    def close(self):
        sys.exit()
