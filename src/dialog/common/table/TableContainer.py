import sys

from src.dialog.common.Dialog import Dialog
from src.dialog.common.DialogContainer import DialogContainer
from src.dialog.common.DialogFactory import DialogFactory
from src.dialog.common.form_doc import FormDocContainer
from src.dialog.common.manage_entity import ManageEntityContainer
from src.dialog.common.manage_entity.ManageEntityDialogMode import ManageEntityDialogMode
from src.dialog.common.table.TableFuncs import TableFuncs
from src.dialog.common.table.data.Table import Table
from src.dialog.common.table.data.TableFactory import TableFactory
from src.session.common.Session import Session
from src.storage.common.entity import EntityStorage


class TableContainer(DialogContainer, TableFuncs):

    def __init__(
            self,
            manage_entity_container: ManageEntityContainer,
            form_doc_container: FormDocContainer,
            session: Session,
            entity_storage: EntityStorage,
            dialog_factory: DialogFactory,
            table_factory: TableFactory
    ):
        super().__init__(dialog_factory)
        self.__manage_entity_container = manage_entity_container
        self.__form_doc_container = form_doc_container
        self.__session = session
        self.__entity_storage = entity_storage
        self.__table_factory = table_factory

        self.__manage_entity_container.set_parent_container(self)
        self.__form_doc_container.set_parent_container(self)

    def create_dialog(self) -> Dialog:
        return self.dialog_factory.create_table_dialog(self)

    def form_doc(self, key: str):
        self.__session.set_form_doc_entity_key(key)
        self.__form_doc_container.show_dialog()

    def create_entity(self):
        self.__session.set_manage_entity_mode(ManageEntityDialogMode.CREATE)
        self.__manage_entity_container.show_dialog()

    def edit_entity(self, key: str):
        self.__session.set_manage_entity_mode(ManageEntityDialogMode.EDIT)
        self.__session.set_edit_entity_id(key)
        self.__manage_entity_container.show_dialog()

    def delete_entity(self, key):
        self.__entity_storage.remove_entity(key)
        self.dialog.draw_table()

    def duplicate_entity(self, key):
        self.__entity_storage.duplicate(key)
        self.dialog.draw_table()

    def get_table_data(self) -> Table:
        return self.__table_factory.create(self.__entity_storage.get_all_entities())

    # Перерисуем таблицу, когда закрывается диалог редактирования сущности
    def child_unfocused(self):
        super().child_unfocused()
        self.dialog.draw_table()
