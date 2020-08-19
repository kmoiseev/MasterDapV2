from abc import abstractmethod
from typing import List


class PickUserFuncs:

    @abstractmethod
    def get_users(self) -> List[str]:
        pass

    @abstractmethod
    def user_selected(self, key):
        pass

    @abstractmethod
    def closed_on_x(self):
        pass
