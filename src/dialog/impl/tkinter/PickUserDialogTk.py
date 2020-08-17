from abc import ABC

from src.dialog.common.pickuser.PickUserDialog import PickUserDialog
from src.dialog.common.pickuser.PickUserFuncs import PickUserFuncs


class PickUserDialogTk(PickUserDialog, ABC):

    def __init__(self, pick_user_funcs: PickUserFuncs):
        super().__init__(pick_user_funcs)

    def draw(self):
        pass

    def close(self):
        pass
