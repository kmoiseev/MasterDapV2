from src.template.property.PropertyTemplate import PropertyTemplate
from src.template.property.PropertyTypeConfig import PropertyTypeConfig


class PropertyTemplateDropdown(PropertyTemplate):

    def __init__(self, property_id: str):
        super().__init__(property_id)
        self.dropdown_name = ''
        self.dropdown_values = []

    def apply_json(self, property_template_json):
        self.dropdown_name = property_template_json["dropdown_name"]

    def apply_config(self, property_type_config: PropertyTypeConfig):
        self.dropdown_values = property_type_config.dropdowns[self.dropdown_name]

