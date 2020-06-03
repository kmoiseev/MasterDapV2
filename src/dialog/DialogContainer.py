from abc import abstractmethod

from src.dialog.Dialog import Dialog
from src.dialog.DialogFactory import DialogFactory


class DialogContainer:

    def __init__(self, dialog_factory: DialogFactory):
        self.dialog_factory = dialog_factory
        self.dialog = None

    @abstractmethod
    def create_dialog(self) -> Dialog:
        pass

    def show_dialog(self):
        self.dialog = self.create_dialog()
        self.dialog.draw()
