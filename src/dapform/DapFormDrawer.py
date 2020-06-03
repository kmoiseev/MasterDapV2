from abc import abstractmethod


class DapFormDrawer:

    @abstractmethod
    def configure_size(self, width: int, height: int):
        pass

    @abstractmethod
    def label(self, text: str):
        pass

    @abstractmethod
    def input(self, ):