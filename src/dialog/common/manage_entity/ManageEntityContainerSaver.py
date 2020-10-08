from typing import Dict, Callable

from src.dialog.common.manage_entity.ManageEntityDialogMode import ManageEntityDialogMode
from src.property.Property import Property
from src.session.common.Session import Session
from src.storage.common.entity.Entity import Entity
from src.storage.common.entity.EntityStorage import EntityStorage


class ManageEntityContainerSaver:

    def __init__(
            self,
            session: Session,
            storage: EntityStorage,
            close_dialog: Callable[[], None],
            show_error: Callable[[str], None]
    ):
        self.__session = session
        self.__storage = storage
        self.__close_dialog = close_dialog
        self.__show_error = show_error

    def save_entity(self, key: str, props: Dict[str, Property]):
        if self.__session.get_manage_entity_mode() == ManageEntityDialogMode.CREATE:
            self.handle_new_entity(key, props)
        elif self.__session.get_manage_entity_mode() == ManageEntityDialogMode.EDIT and \
                self.__session.get_edit_entity_key() != key:
            self.handle_edit_entity_key_changed(key, props)
        elif self.__session.get_manage_entity_mode() == ManageEntityDialogMode.EDIT and \
                self.__session.get_edit_entity_key() == key:
            self.handle_edit_entity_key_unchanged(key, props)

    def handle_new_entity(self, key: str, props: Dict[str, Property]):
        if not self.__storage.check_entity_exists(key):
            self.put_entity_close_dialog(key, props)
        else:
            self.report_entity_exists(key)

    def handle_edit_entity_key_changed(self, key: str, props: Dict[str, Property]):
        if not self.__storage.check_entity_exists(key):
            self.remove_session_entity()
            self.put_entity_close_dialog(key, props)
        else:
            self.report_entity_exists(key)

    def handle_edit_entity_key_unchanged(self, key: str, props: Dict[str, Property]):
        self.put_entity_close_dialog(key, props)

    def put_entity_close_dialog(self, key: str, props: Dict[str, Property]):
        self.__storage.put_entity(
            Entity(key, props)
        )
        self.__close_dialog()

    def remove_session_entity(self):
        self.__storage.remove_entity(self.__session.get_edit_entity_key())

    def report_entity_exists(self, key: str):
        self.__show_error("Дело об АП с номером" + key + " уже существует")
