from typing import Dict, List

from src.dialog.common.Dialog import Dialog
from src.dialog.common.DialogContainer import DialogContainer
from src.dialog.common.DialogFactory import DialogFactory
from src.dialog.common.manage_entity.ManageEntityContainerSaver import ManageEntityContainerSaver
from src.dialog.common.manage_entity.ManageEntityDialogMode import ManageEntityDialogMode
from src.dialog.common.manage_entity.ManageEntityFuncs import ManageEntityFuncs
from src.property.Property import Property
from src.property.PropertyValue import PropertyValue
from src.session.common.Session import Session
from src.storage.common.entity.EntityFactory import EntityFactory
from src.storage.common.entity.EntityStorage import EntityStorage
from src.template.entity.EntityTemplate import EntityTemplate
from src.template.property.PropertyTemplate import PropertyTemplate


class ManageEntityContainer(DialogContainer, ManageEntityFuncs):

    def __init__(
            self,
            session: Session,
            entity_storage: EntityStorage,
            dialog_factory: DialogFactory,
            entity_factory: EntityFactory,
            entity_template: EntityTemplate
    ):
        super().__init__(dialog_factory)
        self.__session = session
        self.__entity_storage = entity_storage
        self.__entity_factory = entity_factory
        self.__entity_template = entity_template

    def create_dialog(self) -> Dialog:
        return self.dialog_factory.create_manage_case_dialog(self)

    def get_mode(self) -> ManageEntityDialogMode:
        return self.__session.get_manage_entity_mode()

    def get_entity_key_property_id(self) -> str:
        return self.__entity_template.key_property

    def get_entity_props_templates(self) -> List[PropertyTemplate]:
        return self.__entity_factory.entity_template.properties_templates

    def get_entity_prop_value(self, prop_id: str) -> PropertyValue:
        return self.__entity_storage.get_entity(self.__session.get_edit_entity_key()).props[prop_id].value

    def save_entity(self, key: str, props: Dict[str, Property]):
        saver = ManageEntityContainerSaver(
            self.__session,
            self.__entity_storage,
            self.close_dialog,
            self.dialog.show_error
        )
        saver.save_entity(key, props)

    def closed_on_x(self):
        self.close_dialog()
