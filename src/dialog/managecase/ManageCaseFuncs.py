from abc import abstractmethod
from typing import Dict


class ManageCaseFuncs:

    @abstractmethod
    def get_case_props(self) -> Dict[str, str]:
        pass

    @abstractmethod
    def save_case(self, key: str, props: Dict[str, str]):
        pass
