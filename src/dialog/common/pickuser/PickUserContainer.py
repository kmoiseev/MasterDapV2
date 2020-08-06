import sys
from typing import List

from src.dialog.common.Dialog import Dialog
from src.dialog.common.DialogContainer import DialogContainer
from src.dialog.common.DialogFactory import DialogFactory
from src.dialog.common.pickuser.PickUserFuncs import PickUserFuncs
from src.session.Session import Session
from src.storage.config.ConfigStorage import ConfigStorage


class PickUserContainer(DialogContainer, PickUserFuncs):

    def __init__(
            self,
            table_container: DialogContainer,
            config_storage: ConfigStorage,
            session: Session,
            dialog_factory: DialogFactory
    ):
        super().__init__(dialog_factory)
        self.__table_container = table_container
        self.__config_storage = config_storage
        self.__session = session

    def get_user_names(self) -> List[str]:
        return self.__config_storage.get_employees_names()

    def user_selected(self, key):
        self.__session.set_employee_id(key)
        self.dialog.close()
        self.__table_container.show_dialog()

    def closed_on_x(self):
        sys.exit()

    def create_dialog(self) -> Dialog:
        return self.dialog_factory.create_pick_user_dialog(self)
