from src.template.property.PropertyTemplate import PropertyTemplate
from src.template.property.PropertyType import PropertyType
from src.template.property.PropertyTypeConfig import PropertyTypeConfig


class PropertyTemplateFactory:

    def __init__(self, property_type_config: PropertyTypeConfig):
        self.type_config = property_type_config

    def load_property_template(self, json) -> PropertyTemplate:
        property_type: PropertyType = PropertyType[json['type']]
        property_template_class = property_type.value
        res = property_template_class(json['id'])
        res.apply_json(json)
        res.apply_config(self.type_config)
        return res
