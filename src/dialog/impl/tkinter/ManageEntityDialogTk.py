from tkinter import Tk
from typing import List

from src.dialog.common.manageentity.ManageEntityDialog import ManageEntityDialog
from src.dialog.common.manageentity.ManageEntityDialogMode import ManageEntityDialogMode
from src.dialog.common.manageentity.ManageEntityFuncs import ManageEntityFuncs
from src.template.property.PropertyTemplate import PropertyTemplate
from src.widget.property.impl.PropertyWidgetFactoryTk import PropertyWidgetFactoryTk
from src.widget.property.impl.PropertyWidgetTk import PropertyWidgetTk


class ManageEntityDialogTk(ManageEntityDialog):

    def __init__(self, manage_entity_funcs: ManageEntityFuncs):
        super().__init__(manage_entity_funcs)
        self.root = Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.funcs.closed_on_x)

    def show(self):

        if self.funcs.get_mode() == ManageEntityDialogMode.CREATE:
            self.root.title("New Case")
        else:
            self.root.title("Edit Case")

        props: List[PropertyTemplate] = self.funcs.get_entity_props_templates()

        widgets: List[PropertyWidgetTk] = list(map(
            PropertyWidgetFactoryTk.create,
            props
        ))

        for rn, widget in enumerate(widgets):
            widget.make(self.root, rn)

        if self.funcs.get_mode() == ManageEntityDialogMode.EDIT:
            for widget in widgets:
                widget.set_val(self.funcs.get_entity_prop_value(widget.prop_tmpl.id))

        self.root.mainloop()

    def show_error(self, message: str):
        pass

    def close(self):
        self.root.destroy()
