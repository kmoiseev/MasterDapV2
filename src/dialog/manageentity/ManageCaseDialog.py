from abc import ABCMeta

from src.dialog.Dialog import Dialog
from src.dialog.manageentity.ManageEntityFuncs import ManageEntityFuncs


class ManageCaseDialog(Dialog, metaclass=ABCMeta):

    def __init__(self, manage_case_funcs: ManageEntityFuncs):
        self.__funcs = manage_case_funcs
