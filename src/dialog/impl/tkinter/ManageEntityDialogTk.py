from tkinter import Tk, Button, messagebox
from typing import List, Dict

from src.dialog.common.manage_entity.ManageEntityDialog import ManageEntityDialog
from src.dialog.common.manage_entity.ManageEntityDialogMode import ManageEntityDialogMode
from src.dialog.common.manage_entity.ManageEntityFuncs import ManageEntityFuncs
from src.property.Property import Property
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
            text_button = "Save"
        else:
            self.root.title("Edit Case")
            text_button = "Edit"

        props_templates: List[PropertyTemplate] = self.funcs.get_entity_props_templates()

        widgets: List[PropertyWidgetTk] = list(map(
            PropertyWidgetFactoryTk.create,
            props_templates
        ))

        for rn, widget in enumerate(widgets):
            widget.make(self.root, rn)

        if self.funcs.get_mode() == ManageEntityDialogMode.EDIT:
            for widget in widgets:
                widget.set_val(self.funcs.get_entity_prop_value(widget.prop_tmpl.id))

        Button(self.root, text=text_button, command=lambda: self.save_entity(widgets)).grid()

        self.root.mainloop()

    def save_entity(self, widgets: List[PropertyWidgetTk]):
        properties_for_save: Dict[str, Property] = {
            widgets[i].prop_tmpl.id: Property(widgets[i].prop_tmpl, widgets[i].get_val())
            for i in range(0, len(widgets))
        }
        self.funcs.save_entity(
            properties_for_save[self.funcs.get_entity_key_property_id()].get_val(),
            properties_for_save
        )

    def show_error(self, message: str):
        messagebox.showerror("Ошибка", message)
        pass

    def close(self):
        self.root.destroy()
