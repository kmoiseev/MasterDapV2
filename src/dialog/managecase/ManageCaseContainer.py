from typing import Dict

from src.dialog.Dialog import Dialog
from src.dialog.DialogContainer import DialogContainer
from src.dialog.DialogFactory import DialogFactory
from src.dialog.managecase.ManageCaseFuncs import ManageCaseFuncs
from src.session.Session import Session
from src.storage.case.CaseStorage import CaseStorage


class ManageCaseContainer(DialogContainer, ManageCaseFuncs):

    def __init__(self, session: Session, case_storage: CaseStorage, dialog_factory: DialogFactory):
        super().__init__(dialog_factory)
        self.__session = session
        self.__case_storage = case_storage

    def get_case_props(self) -> Dict[str, str]:
        return self.__case_storage.get_case(self.__session.get_case_id()).props

    def save_case(self, key: str, props: Dict[str, str]):
        self.__case_storage.put_case(key, props)
        self.dialog.close()

    def create_dialog(self) -> Dialog:
        return self.dialog_factory.create_manage_case_dialog(self)
