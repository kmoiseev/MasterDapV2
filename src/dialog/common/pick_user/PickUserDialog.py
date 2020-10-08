from abc import ABCMeta

from src.dialog.common.Dialog import Dialog
from src.dialog.common.pick_user.PickUserFuncs import PickUserFuncs


class PickUserDialog(Dialog, metaclass=ABCMeta):

    def __init__(self, pick_user_funcs: PickUserFuncs):
        self.funcs = pick_user_funcs
