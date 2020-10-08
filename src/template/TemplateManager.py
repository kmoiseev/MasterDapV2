from src.template.doc.DocsTemplates import DocsTemplates
from src.template.entity.EntityTemplate import EntityTemplate
from src.template.property.PropertyTemplateFactory import PropertyTemplateFactory
from src.template.property.PropertyTypeConfig import PropertyTypeConfig
from src.template.table.TableTemplate import TableTemplate
from src.template.user.UserTemplate import UserTemplate
from src.util.json.JsonReader import JsonReader


class TemplateManager:

    def __init__(self, template_folder, property_type_config: PropertyTypeConfig):
        self.property_template_factory = PropertyTemplateFactory(property_type_config)
        self.user_template = UserTemplate(
            JsonReader(template_folder + 'user_template.json').read(),
            self.property_template_factory
        )
        self.entity_template = EntityTemplate(
            JsonReader(template_folder + 'entity_template.json').read(),
            self.property_template_factory
        )
        self.table_template = TableTemplate(
            JsonReader(template_folder + 'table_template.json').read()
        )
        self.docs_templates = DocsTemplates(
            JsonReader(template_folder + 'doc_template.json').read(),
            self.property_template_factory
        )
