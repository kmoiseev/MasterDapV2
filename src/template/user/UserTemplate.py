from typing import List

from src.template.property.PropertyTemplate import PropertyTemplate
from src.template.property.PropertyTemplateFactory import PropertyTemplateFactory


class UserTemplate:

    def __init__(self, user_template_json, property_template_factory: PropertyTemplateFactory):
        self.properties_templates: List[PropertyTemplate] = list(map(
            lambda property_template_json:
            property_template_factory.load_property_template(property_template_json),
            user_template_json['properties']
        ))
