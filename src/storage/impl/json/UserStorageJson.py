from typing import Dict

from src.storage.common.user.UserFactory import UserFactory
from src.storage.common.user.UserStorage import UserStorage
from src.util.json.JsonReader import JsonReader


class UserStorageJson(UserStorage):

    def __init__(self, file_path: str, user_factory: UserFactory):
        super().__init__(user_factory)
        self.__file_path = file_path

    def get_users(self):
        user_json: Dict = JsonReader(self.__file_path).read()
        res = []
        for user in user_json.keys():
            res.append(self.user_factory.create(user, user_json[user]))
        return res

    def get_user_by_key(self, key: str):
        config_json = JsonReader(self.__file_path).read()
        return config_json["employees"][key]
