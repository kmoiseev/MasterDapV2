from typing import List, Dict

from src.storage.common.entity.Entity import Entity
from src.storage.common.entity.EntityStorage import EntityStorage
from src.util.json.JsonReader import JsonReader
from src.util.json.JsonWriter import JsonWriter


class EntityStorageJson(EntityStorage):

    def __init__(self, file_path: str):
        self.__file_path = file_path

    def get_all_entities(self) -> List[Entity]:
        pass

    def put_entity(self, entity: Entity):
        entities_json = JsonReader(self.__file_path).read()
        entities_json[entity.key] = entity.props
        JsonWriter(self.__file_path, entities_json).write()

    def get_entity(self, key) -> Entity:
        entities_json = JsonReader(self.__file_path).read()
        return Entity(key, entities_json[key])

    def remove_entity(self, key):
        entities_json = JsonReader(self.__file_path).read()
        del entities_json[key]
        JsonWriter(self.__file_path, entities_json).write()