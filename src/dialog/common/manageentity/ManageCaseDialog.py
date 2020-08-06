from abc import ABCMeta

from src.dialog.common.Dialog import Dialog
from src.dialog.common.manageentity import ManageEntityFuncs


class ManageCaseDialog(Dialog, metaclass=ABCMeta):

    def __init__(self, manage_case_funcs: ManageEntityFuncs):
        self.__funcs = manage_case_funcs
