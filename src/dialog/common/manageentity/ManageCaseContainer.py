from typing import Dict

from src.dialog.common.Dialog import Dialog
from src.dialog.common.DialogContainer import DialogContainer
from src.dialog.common.DialogFactory import DialogFactory
from src.dialog.common.manageentity import ManageEntityFuncs
from src.session.Session import Session
from src.storage.entity.EntityStorage import EntityStorage


class ManageEntityContainer(DialogContainer, ManageEntityFuncs):

    def __init__(self, session: Session, case_storage: EntityStorage, dialog_factory: DialogFactory):
        super().__init__(dialog_factory)
        self.__session = session
        self.__case_storage = case_storage

    def get_entity_props(self) -> Dict[str, str]:
        return self.__case_storage.get_entity(self.__session.get_case_id()).props

    def save_entity(self, key: str, props: Dict[str, str]):
        self.__case_storage.put_entity(key, props)
        self.dialog.close()

    def create_dialog(self) -> Dialog:
        return self.dialog_factory.create_manage_case_dialog(self)
