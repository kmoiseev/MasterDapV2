from abc import ABCMeta

from src.dialog.Dialog import Dialog
from src.dialog.pickuser.PickUserFuncs import PickUserFuncs


class PickUserDialog(Dialog, metaclass=ABCMeta):

    def __init__(self, pick_user_funcs: PickUserFuncs):
        self.__funcs = pick_user_funcs
