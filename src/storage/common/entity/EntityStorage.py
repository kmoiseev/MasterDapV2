from abc import abstractmethod
from typing import List, Dict

from src.storage.common.entity.EntityFactory import EntityFactory
from src.storage.common.entity.Entity import Entity
from src.storage.common.entity.EntitySerializer import EntitySerializer
from src.template.entity.EntityTemplate import EntityTemplate


class EntityStorage:

    def __init__(self, entity_template: EntityTemplate):
        self.entity_factory = EntityFactory(entity_template)
        self.entity_serializer = EntitySerializer()

    @abstractmethod
    def get_all_entities(self) -> List[Entity]:
        pass

    @abstractmethod
    def put_entity(self, entity: Entity):
        pass

    @abstractmethod
    def get_entity(self, key) -> Entity:
        pass

    @abstractmethod
    def remove_entity(self, key):
        pass
