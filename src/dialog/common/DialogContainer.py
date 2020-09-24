from abc import abstractmethod

from src.dialog.common.Dialog import Dialog
from src.dialog.common.DialogFactory import DialogFactory


class DialogContainer:

    def __init__(self, dialog_factory: DialogFactory):
        self.dialog_factory = dialog_factory
        self.dialog = None
        self.parent_container = None

    @abstractmethod
    def create_dialog(self) -> Dialog:
        pass

    def show_dialog(self):
        if self.parent_container is not None:
            self.parent_container.child_focused()

        self.dialog = self.create_dialog()
        self.dialog.show()

    def close_dialog(self):
        if self.parent_container is not None:
            self.parent_container.child_unfocused()

        self.dialog.close()
        self.dialog = None

    def set_parent_container(self, parent_container):
        self.parent_container = parent_container

    def child_focused(self):
        self.dialog.disable()

    def child_unfocused(self):
        self.dialog.enable()
