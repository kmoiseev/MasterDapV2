from abc import abstractmethod
from typing import Dict


class ManageEntityFuncs:

    @abstractmethod
    def get_entity_props(self) -> Dict[str, str]:
        pass

    @abstractmethod
    def save_entity(self, key: str, props: Dict[str, str]):
        pass
