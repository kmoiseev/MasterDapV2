from abc import abstractmethod
from typing import List, Dict

from src.storage.case.Case import Case


class CaseStorage:

    @abstractmethod
    def get_all_cases(self) -> List[Case]:
        pass

    @abstractmethod
    def put_case(self, key: str, props: Dict[str, str]):
        pass

    @abstractmethod
    def get_case(self, key) -> Case:
        pass

    @abstractmethod
    def remove_case(self, key):
        pass
