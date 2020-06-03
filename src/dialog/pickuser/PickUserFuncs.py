from abc import abstractmethod
from typing import List


class PickUserFuncs:

    @abstractmethod
    def get_user_names(self) -> List[str]:
        pass

    @abstractmethod
    def user_selected(self, key):
        pass

    @abstractmethod
    def closed_on_x(self):
        pass
