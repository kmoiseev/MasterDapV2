from typing import List

from src.dialog.Dialog import Dialog
from src.dialog.DialogContainer import DialogContainer
from src.dialog.DialogFactory import DialogFactory
from src.dialog.formdoc.FormDocContainer import FormDocContainer
from src.dialog.manageentity.ManageCaseContainer import ManageEntityContainer
from src.dialog.table.TableFuncs import TableFuncs
from src.session.Session import Session
from src.storage.entity.Entity import Entity
from src.storage.entity.EntityStorage import EntityStorage


class TableContainer(DialogContainer, TableFuncs):

    def __init__(
            self,
            manage_case_container: ManageEntityContainer,
            form_doc_container: FormDocContainer,
            session: Session,
            case_storage: EntityStorage,
            dialog_factory: DialogFactory
    ):
        super().__init__(dialog_factory)
        self.__manage_case_container = manage_case_container
        self.__form_doc_container = form_doc_container
        self.__session = session
        self.__case_storage = case_storage

    def form_doc(self, key: str):
        self.__session.set_case_id(key)
        self.__form_doc_container.show_dialog()

    def create_deal(self):
        self.__session.set_case_id("")
        self.__manage_case_container.show_dialog()

    def edit_deal(self, key: str):
        self.__session.set_case_id(key)
        self.__manage_case_container.show_dialog()

    def delete_deal(self, key):
        self.__case_storage.remove_entity(key)

    def get_table_data(self) -> List[Entity]:
        return self.__case_storage.get_all_entities()

    def create_dialog(self) -> Dialog:
        return self.__dialog_factory.create_table_dialog(self)
