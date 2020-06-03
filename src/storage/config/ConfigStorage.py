from abc import abstractmethod
from typing import List, Dict


class ConfigStorage:

    @abstractmethod
    def get_employees_names(self) -> List[str]:
        pass

    @abstractmethod
    def get_employee_by_key(self, key: str) -> Dict[str, str]:
        pass
