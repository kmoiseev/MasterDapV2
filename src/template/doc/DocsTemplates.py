from src.template.doc.DocTemplate import DocTemplate
from src.template.property.PropertyTemplateFactory import PropertyTemplateFactory


class DocsTemplates:

    def __init__(self, docs_templates_json, property_template_factory: PropertyTemplateFactory):
        self.templates = list(map(
            lambda property_template_json:
            DocTemplate(property_template_json, property_template_factory),
            docs_templates_json['docs']
        ))
