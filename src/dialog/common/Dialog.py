from abc import abstractmethod


class Dialog:

    @abstractmethod
    def show(self):
        pass

    def close(self):
        pass

    def enable(self):
        pass

    def disable(self):
        pass
