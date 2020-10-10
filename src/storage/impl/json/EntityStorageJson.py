from typing import List, Dict

from src.storage.common.entity import EntityFactory
from src.storage.common.entity.Entity import Entity
from src.storage.common.entity.EntitySerializer import EntitySerializer
from src.storage.common.entity.EntityStorage import EntityStorage
from src.util.json.JsonReader import JsonReader
from src.util.json.JsonWriter import JsonWriter


class EntityStorageJson(EntityStorage):

    def __init__(self, file_path: str, entity_factory: EntityFactory):
        super().__init__(entity_factory)
        self.__file_path = file_path

    def get_all_entities(self) -> List[Entity]:
        entities_json: Dict = JsonReader(self.__file_path).read()
        return \
            list(map(
                lambda entity_key: self.entity_factory.create(
                    entity_key,
                    entities_json[entity_key]
                ),
                entities_json.keys()
            ))

    def put_entity(self, entity: Entity):
        entities_json = JsonReader(self.__file_path).read()
        entities_json[entity.key] = EntitySerializer.serialize(entity.props)
        JsonWriter(self.__file_path, entities_json).write()

    def check_entity_exists(self, key: str) -> bool:
        entities_json: Dict = JsonReader(self.__file_path).read()
        return key in entities_json

    def get_entity(self, key) -> Entity:
        entities_json = JsonReader(self.__file_path).read()
        return self.entity_factory.create(
            key,
            entities_json[key]
        )

    def remove_entity(self, key):
        entities_json = JsonReader(self.__file_path).read()
        del entities_json[key]
        JsonWriter(self.__file_path, entities_json).write()

    def duplicate(self, key):
        entities_json = JsonReader(self.__file_path).read()
        self.entity_factory.create(
            str(int(key)+1),
            entities_json[key])
        JsonWriter(self.__file_path, entities_json).write()
        # todo
