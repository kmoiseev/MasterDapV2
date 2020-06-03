from typing import List

from src.dialog.Dialog import Dialog
from src.dialog.DialogContainer import DialogContainer
from src.dialog.DialogFactory import DialogFactory
from src.dialog.formdoc.FormDocContainer import FormDocContainer
from src.dialog.managecase.ManageCaseContainer import ManageCaseContainer
from src.dialog.table.TableFuncs import TableFuncs
from src.dialog.table.data.TableRow import TableRow
from src.session.Session import Session
from src.storage.case.Case import Case
from src.storage.case.CaseStorage import CaseStorage


class TableContainer(DialogContainer, TableFuncs):

    def __init__(
            self,
            manage_case_container: ManageCaseContainer,
            form_doc_container: FormDocContainer,
            session: Session,
            case_storage: CaseStorage,
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
        self.__case_storage.remove_case(key)

    def get_table_data(self) -> List[Case]:
        return self.__case_storage.get_all_cases()

    def _create_dialog(self) -> Dialog:
        return self.__dialog_factory.create_table_dialog(self)
