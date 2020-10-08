from abc import ABCMeta, abstractmethod

from src.dialog.common.Dialog import Dialog
from src.dialog.common.manage_entity import ManageEntityFuncs


class ManageEntityDialog(Dialog, metaclass=ABCMeta):

    def __init__(self, manage_entity_funcs: ManageEntityFuncs):
        self.funcs = manage_entity_funcs

    @abstractmethod
    def show_error(self, message: str):
        pass
