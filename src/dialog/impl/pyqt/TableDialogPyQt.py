import sys

from PyQt5 import Qt
from PyQt5.QtGui import QPalette, QColor

from abc import ABC

from PyQt5.QtWidgets import QWidget

from src.dialog.common.table.TableDialog import TableDialog
from src.dialog.common.table.TableFuncs import TableFuncs
from src.dialog.common.table.data.Table import Table
from src.dialog.common.table.TableContainer import TableContainer
from src.dialog.impl.pyqt.ButtonUtils import create_qt_button
from src.template.TemplateManager import TemplateManager
from src.template.table.TableTemplate import TableTemplate
from src.storage.Icons import *


class TableDialogPyQt(TableDialog, ABC):

    def __init__(self, table_funcs: TableFuncs):
        super().__init__(table_funcs)

    def show(self):
        table: Table = self.funcs.get_table_data()

        class ManageDealsWidget(QWidget):

            def __init__(self):
                super().__init__()

                def create_button_callback():
                    manage_deals_widget.setDisabled(True)
                    # ?????????
                    # TableContainer.create_deal()

                def edit_button_callback(deal_number, deal_json):
                    pass

                def delete_button_callback(chosen_deal_number):
                    pass

                def run_create_docs(chosen_deal, chosen_employee):
                    pass

                layout = Qt.QVBoxLayout(self)
                icon_create = Qt.QIcon(CREATE)
                icon_form = Qt.QIcon(FORM)
                icon_edit = Qt.QIcon(EDIT)
                icon_delete = Qt.QIcon(DELETE)

                create_case_button = create_qt_button(icon_create, create_button_callback, "Создать ДАП")
                create_case_button.setFixedWidth(110)
                create_case_button.setFixedHeight(30)
                layout.addWidget(create_case_button)

                labels = list(map(lambda cell: cell.value, table.header.cells))
                table_widget = Qt.QTableWidget(0, len(labels))
                table_widget.setColumnHidden(len(labels), False)
                table_widget.setHorizontalHeaderLabels(labels)
                for k, row in enumerate(table.rows):
                    table_widget.insertRow(table_widget.rowCount())
                    for j, cell in enumerate(row.cells):
                        table_widget.setItem(k, j, Qt.QTableWidgetItem(cell.value))
                        create_deal_button = create_qt_button(icon_form, run_create_docs, "Сформировать")
                        edit_deal_button = create_qt_button(icon_edit, edit_button_callback)
                        delete_deal_button = create_qt_button(icon_delete, delete_button_callback)
                        table_widget.setCellWidget(j, 0, create_deal_button)
                        table_widget.setCellWidget(j, 1, edit_deal_button)
                        table_widget.setCellWidget(j, 2, delete_deal_button)
                        if j == 7 or j == 8:
                            table_widget.item(k, j).setBackground(QColor('orange' if cell.red else 'green'))
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
