from abc import abstractmethod


class Dialog:

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def close(self):
        pass
