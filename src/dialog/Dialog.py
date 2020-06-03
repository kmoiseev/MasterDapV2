from abc import abstractmethod


class Dialog:

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def close(self):
        pass
