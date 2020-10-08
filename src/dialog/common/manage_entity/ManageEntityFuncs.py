from abc import abstractmethod
from typing import Dict, List

from src.dialog.common.manage_entity.ManageEntityDialogMode import ManageEntityDialogMode
from src.property.Property import Property
from src.property.PropertyValue import PropertyValue
from src.template.property.PropertyTemplate import PropertyTemplate


class ManageEntityFuncs:

    @abstractmethod
    def get_mode(self) -> ManageEntityDialogMode:
        pass

    @abstractmethod
    def get_entity_key_property_id(self) -> str:
        pass

    def get_entity_props_templates(self) -> List[PropertyTemplate]:
        pass

    @abstractmethod
    def get_entity_prop_value(self, prop_id: str) -> PropertyValue:
        pass

    @abstractmethod
    def save_entity(self, key: str, props: Dict[str, Property]):
        pass

    @abstractmethod
    def closed_on_x(self):
        pass
