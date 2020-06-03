from abc import ABCMeta

from src.dialog.Dialog import Dialog
from src.dialog.managecase.ManageCaseFuncs import ManageCaseFuncs


class ManageCaseDialog(Dialog, metaclass=ABCMeta):

    def __init__(self, manage_case_funcs: ManageCaseFuncs):
        self.__funcs = manage_case_funcs
