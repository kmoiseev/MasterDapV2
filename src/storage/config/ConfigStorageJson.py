from src.storage.config.ConfigStorage import ConfigStorage
from src.storage.json.JsonUtil import read_json


class ConfigStorageJson(ConfigStorage):

    def __init__(self, file_path: str):
        self.__file_path = file_path

    def get_employees_names(self):
        config_json = read_json(self.__file_path)
        res = []
        for employee in config_json["employees"]:
            res.append(employee["ip"])
        return res

    def get_employee_by_key(self, key: str):
        config_json = read_json(self.__file_path)
        return config_json["employees"][key]
