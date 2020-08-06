from abc import abstractmethod


class Dialog:

    def __init__(self, dap_form_path):
        self.dap_form_path = dap_form_path

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def close(self):
        pass
