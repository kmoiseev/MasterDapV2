from abc import abstractmethod
from typing import List

from src.storage.common.user.User import User


class PickUserFuncs:

    @abstractmethod
    def get_users(self) -> List[User]:
        pass

    @abstractmethod
    def user_selected(self, key):
        pass

    @abstractmethod
    def closed_on_x(self):
        pass
