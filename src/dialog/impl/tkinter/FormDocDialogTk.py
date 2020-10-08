from tkinter import Tk

from src.dialog.common.formdoc.FormDocDialog import FormDocDialog
from src.dialog.common.formdoc.FormDocFuncs import FormDocFuncs


class FormDocDialogTk(FormDocDialog):

    def __init__(self, form_doc_funcs: FormDocFuncs):
        super().__init__(form_doc_funcs)
        self.root = Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.funcs.closed_on_x)

    def show(self):
        self.root.title(self.funcs.get_form_doc_entity_id())
        self.root.mainloop()

    def close(self):
        self.root.destroy()
