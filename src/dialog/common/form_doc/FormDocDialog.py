from abc import ABCMeta

from src.dialog.common.Dialog import Dialog
from src.dialog.common.form_doc import FormDocFuncs


class FormDocDialog(Dialog, metaclass=ABCMeta):

    def __init__(self, form_doc_funcs: FormDocFuncs):
        super().__init__()
        self.funcs = form_doc_funcs
