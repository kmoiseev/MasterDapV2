from typing import Dict

from src.property.PropertyFactory import PropertyFactory
from src.storage.common.entity.Entity import Entity
from src.template.entity.EntityTemplate import EntityTemplate


class EntityFactory:

    def __init__(self, entity_template: EntityTemplate):
        self.entity_template = entity_template

    def create(self, key: str, props_values: Dict[str, str]) -> Entity:
        return Entity(
            key,
            PropertyFactory.create_from_template_and_dict(
                self.entity_template.properties_templates,
                props_values,
                lambda prop_template_id: 'Property ' + prop_template_id + ' not found for entity ' + key
            )
        )
