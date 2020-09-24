from abc import abstractmethod

from src.property.PropertyValue import PropertyValue
from src.template.property.PropertyTemplate import PropertyTemplate


class PropertyWidget:

    def __init__(self, prop_tmpl: PropertyTemplate):
        self.prop_tmpl = prop_tmpl

    @abstractmethod
    def set_val(self, val: PropertyValue):
        pass

    @abstractmethod
    def get_val(self) -> PropertyValue:
        pass
