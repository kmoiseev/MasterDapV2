from src.template.property.PropertyTypeConfig import PropertyTypeConfig


class PropertyTemplate:

    def __init__(self, property_id: str):
        self.id = property_id

    def apply_json(self, property_template_json):
        pass

    def apply_config(self, property_type_config: PropertyTypeConfig):
        pass
