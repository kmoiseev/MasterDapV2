from typing import List, Dict

from src.storage.case.Case import Case
from src.storage.case.CaseStorage import CaseStorage
from src.storage.json.JsonUtil import read_json, write_json


class CaseStorageJson(CaseStorage):

    def __init__(self, file_path: str):
        self.__file_path = file_path

    def get_all_cases(self) -> List[Case]:
        pass

    def put_case(self, key: str, props: Dict[str, str]):
        cases_json = read_json(self.__file_path)
        cases_json[key] = props
        write_json(self.__file_path, cases_json)

    def get_case(self, key) -> Case:
        cases_json = read_json(self.__file_path)
        return Case(key, cases_json[key])

    def remove_case(self, key):
        cases_json = read_json(self.__file_path)
        del cases_json[key]
        write_json(self.__file_path, cases_json)