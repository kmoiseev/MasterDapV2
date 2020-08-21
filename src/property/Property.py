from src.property.PropertyValue import PropertyValue
from src.template.property.PropertyTemplate import PropertyTemplate


class Property:

    def __init__(self, template: PropertyTemplate, value: PropertyValue):
        self.template = template
        self.value = value

    def get_id(self):
        return self.template.id

    def set_val(self, val: str):
        self.value = PropertyValue(val)

    def get_val(self) -> str:
        return self.value.value
