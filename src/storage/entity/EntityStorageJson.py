from typing import List, Dict

from src.storage.entity.Entity import Entity
from src.storage.entity.EntityStorage import EntityStorage
from src.storage.json.JsonUtil import read_json, write_json


class EntityStorageJson(EntityStorage):

    def __init__(self, file_path: str):
        self.__file_path = file_path

    def get_all_entities(self) -> List[Entity]:
        pass

    def put_entity(self, key: str, props: Dict[str, str]):
        cases_json = read_json(self.__file_path)
        cases_json[key] = props
        write_json(self.__file_path, cases_json)

    def get_entity(self, key) -> Entity:
        cases_json = read_json(self.__file_path)
        return Entity(key, cases_json[key])

    def remove_entity(self, key):
        cases_json = read_json(self.__file_path)
        del cases_json[key]
        write_json(self.__file_path, cases_json)