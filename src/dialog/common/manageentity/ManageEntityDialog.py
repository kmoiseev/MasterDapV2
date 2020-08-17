from abc import ABCMeta

from src.dialog.common.Dialog import Dialog
from src.dialog.common.manageentity import ManageEntityFuncs


class ManageEntityDialog(Dialog, metaclass=ABCMeta):

    def __init__(self, manage_entity_funcs: ManageEntityFuncs):
        self.funcs = manage_entity_funcs
