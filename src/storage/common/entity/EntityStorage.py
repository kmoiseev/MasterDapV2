from abc import abstractmethod
from typing import List, Dict

from src.storage.common.entity.Entity import Entity


class EntityStorage:

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
