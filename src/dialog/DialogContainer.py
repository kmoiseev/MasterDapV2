from abc import abstractmethod

from src.dialog.Dialog import Dialog
from src.dialog.DialogFactory import DialogFactory


class DialogContainer:

    def __init__(self, dialog_factory: DialogFactory):
        self.__dialog_factory = dialog_factory
        self.__dialog = None

    @abstractmethod
    def _create_dialog(self) -> Dialog:
        pass

    def show_dialog(self):
        self.__dialog = self._create_dialog()
        self.__dialog.draw()
