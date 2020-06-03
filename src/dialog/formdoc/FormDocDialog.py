from abc import ABCMeta

from src.dialog.Dialog import Dialog
from src.dialog.formdoc.FormDocFuncs import FormDocFuncs


class FormDocDialog(Dialog, metaclass=ABCMeta):

    def __init__(self, form_doc_funcs: FormDocFuncs):
        self._form_doc_funcs = form_doc_funcs
