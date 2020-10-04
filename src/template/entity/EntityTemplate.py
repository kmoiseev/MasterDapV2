from src.template.property.PropertyTemplateFactory import PropertyTemplateFactory


class EntityTemplate:

    def __init__(self, user_template_json, property_template_factory: PropertyTemplateFactory):
        self.key_property = user_template_json['key_property']
        self.properties_templates = list(map(
            lambda property_template_json:
            property_template_factory.load_property_template(property_template_json),
            user_template_json['properties']
        ))
