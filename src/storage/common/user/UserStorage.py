from abc import abstractmethod
from typing import List

from src.storage.common.user.User import User
from src.storage.common.user.UserFactory import UserFactory


class UserStorage:

    def __init__(self, user_factory: UserFactory):
        self.user_factory = user_factory

    @abstractmethod
    def get_users(self) -> List[User]:
        pass

    @abstractmethod
    def get_user_by_key(self, key: str) -> User:
        pass
