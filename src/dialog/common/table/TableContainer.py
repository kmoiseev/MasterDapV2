from src.dialog.common.Dialog import Dialog
from src.dialog.common.DialogContainer import DialogContainer
from src.dialog.common.DialogFactory import DialogFactory
from src.dialog.common.formdoc import FormDocContainer
from src.dialog.common.manageentity import ManageEntityContainer
from src.dialog.common.table.TableFuncs import TableFuncs
from src.dialog.common.table.data.Table import Table
from src.session.common.Session import Session
from src.storage.common.entity import EntityStorage


class TableContainer(DialogContainer, TableFuncs):

    def __init__(
            self,
            manage_entity_container: ManageEntityContainer,
            form_doc_container: FormDocContainer,
            session: Session,
            entity_storage: EntityStorage,
            dialog_factory: DialogFactory
    ):
        super().__init__(dialog_factory)
        self.__manage_case_container = manage_entity_container
        self.__form_doc_container = form_doc_container
        self.__session = session
        self.__entity_storage = entity_storage

    def form_doc(self, key: str):
        self.__session.set_form_doc_entity_id(key)
        self.__form_doc_container.show_dialog()

    def create_deal(self):
        self.__session.set_edit_entity_id("")
        self.__manage_case_container.show_dialog()

    def edit_deal(self, key: str):
        self.__session.set_edit_entity_id(key)
        self.__manage_case_container.show_dialog()

    def delete_deal(self, key):
        self.__entity_storage.remove_entity(key)

    def get_table_data(self) -> Table:
        return Table()
        return self.__entity_storage.get_all_entities()

    def create_dialog(self) -> Dialog:
        return self.dialog_factory.create_table_dialog(self)
