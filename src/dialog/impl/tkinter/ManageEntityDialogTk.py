from tkinter import Tk
from typing import List

from src.dialog.common.manageentity.ManageEntityDialog import ManageEntityDialog
from src.dialog.common.manageentity.ManageEntityDialogMode import ManageEntityDialogMode
from src.dialog.common.manageentity.ManageEntityFuncs import ManageEntityFuncs
from src.template.property.PropertyTemplate import PropertyTemplate


class ManageEntityDialogTk(ManageEntityDialog):

    def __init__(self, manage_entity_funcs: ManageEntityFuncs):
        super().__init__(manage_entity_funcs)
        self.root = Tk()

    def show(self):

        if self.funcs.get_mode() == ManageEntityDialogMode.CREATE:
            self.root.title("New Case")
        else:
            self.root.title("Edit Case")

        props: List[PropertyTemplate] = self.funcs.get_entity_props_templates()

        # Итерируешь по props и на основе PropertyTemplate строишь поля ввода
        # если режим - ManageEntityDialogMode.CREATE - то также вызываешь
        # self.funcs.get_entity_prop_value(ключ свойства)

        self.root.mainloop()

    def show_error(self, message: str):
        pass

    def close(self):
        self.root.destroy()
