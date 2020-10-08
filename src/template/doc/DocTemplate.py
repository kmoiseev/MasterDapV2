from src.template.property.PropertyTemplateFactory import PropertyTemplateFactory


class DocTemplate:

    def __init__(self, doc_template_json, property_template_factory: PropertyTemplateFactory):
        self.id = doc_template_json['id']
        self.name = doc_template_json['name']
        self.properties_templates = list(map(
            lambda property_template_json:
            property_template_factory.load_property_template(property_template_json),
            doc_template_json['properties']
        ))
