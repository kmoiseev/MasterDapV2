from tkinter import Tk

from src.dialog.common.manageentity.ManageEntityDialog import ManageEntityDialog
from src.dialog.common.manageentity.ManageEntityFuncs import ManageEntityFuncs


class ManageEntityDialogTk(ManageEntityDialog):

    def __init__(self, manage_entity_funcs: ManageEntityFuncs):
        super().__init__(manage_entity_funcs)
        self.root = Tk()

    def show(self):
        self.root.title("New Case")
        self.root.mainloop()

    def close(self):
        self.root.destroy()
