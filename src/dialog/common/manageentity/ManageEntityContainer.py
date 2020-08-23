from typing import Dict

from src.dialog.common.Dialog import Dialog
from src.dialog.common.DialogContainer import DialogContainer
from src.dialog.common.DialogFactory import DialogFactory
from src.dialog.common.manageentity.ManageEntityFuncs import ManageEntityFuncs
from src.session.common.Session import Session
from src.storage.common.entity.EntityStorage import EntityStorage


class ManageEntityContainer(DialogContainer, ManageEntityFuncs):

    def __init__(self, session: Session, entity_storage: EntityStorage, dialog_factory: DialogFactory):
        super().__init__(dialog_factory)
        self.__session = session
        self.__entity_storage = entity_storage

    def get_entity_props(self) -> Dict[str, str]:
        return self.__entity_storage.get_entity(self.__session.get_edit_entity_id()).props

    def save_entity(self, key: str, props: Dict[str, str]):
        self.__entity_storage.put_entity(key, props)
        self.dialog.close()

    def create_dialog(self) -> Dialog:
        return self.dialog_factory.create_manage_case_dialog(self)
