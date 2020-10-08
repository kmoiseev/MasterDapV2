from tkinter import Tk, Label, Button
from typing import List

from src.dialog.common.form_doc.FormDocDialog import FormDocDialog
from src.dialog.common.form_doc.FormDocFuncs import FormDocFuncs
from src.template.doc.DocTemplate import DocTemplate
from src.widget.property.impl.PropertyWidgetFactoryTk import PropertyWidgetFactoryTk
from src.widget.property.impl.PropertyWidgetTk import PropertyWidgetTk


class FormDocDialogTk(FormDocDialog):

    def __init__(self, form_doc_funcs: FormDocFuncs):
        super().__init__(form_doc_funcs)
        self.root = Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.funcs.closed_on_x)

    def show(self):
        self.root.title(self.funcs.get_form_doc_entity_key())

        docs_templates: List[DocTemplate] = self.funcs.get_docs_templates()
        rn = 0
        for doc_template in docs_templates:
            rn = self.draw_doc(doc_template, rn)

        Button(self.root, text='Сформировать', command=lambda: self.funcs.form_doc(
            {}
        )).grid()

        self.root.mainloop()

    def draw_doc(self, template: DocTemplate, rn: int) -> int:

        lbl = Label(self.root, text=template.name)
        lbl.grid(column=0, row=rn)
        rn += 1

        widgets: List[PropertyWidgetTk] = list(map(
            PropertyWidgetFactoryTk.create,
            template.properties_templates
        ))

        for widget in widgets:
            widget.make(self.root, rn)
            rn += 1

        return rn

    def close(self):
        self.root.destroy()
