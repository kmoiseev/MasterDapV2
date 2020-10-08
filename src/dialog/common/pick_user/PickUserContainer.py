import sys
from typing import List

from src.dialog.common.Dialog import Dialog
from src.dialog.common.DialogContainer import DialogContainer
from src.dialog.common.DialogFactory import DialogFactory
from src.dialog.common.pick_user.PickUserFuncs import PickUserFuncs
from src.session.common.Session import Session
from src.storage.common.user.User import User
from src.storage.common.user.UserStorage import UserStorage


class PickUserContainer(DialogContainer, PickUserFuncs):

    def __init__(
            self,
            table_container: DialogContainer,
            config_storage: UserStorage,
            session: Session,
            dialog_factory: DialogFactory
    ):
        super().__init__(dialog_factory)
        self.__table_container = table_container
        self.__config_storage = config_storage
        self.__session = session

    def create_dialog(self) -> Dialog:
        return self.dialog_factory.create_pick_user_dialog(self)

    def get_users(self) -> List[User]:
        return self.__config_storage.get_users()

    def user_selected(self, key):
        self.__session.set_user_id(key)
        self.close_dialog()
        self.__table_container.show_dialog()

    def closed_on_x(self):
        sys.exit()
