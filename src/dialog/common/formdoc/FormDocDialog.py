from abc import ABCMeta

from src.dialog.common.Dialog import Dialog
from src.dialog.common.formdoc import FormDocFuncs


class FormDocDialog(Dialog, metaclass=ABCMeta):

    def __init__(self, form_doc_funcs: FormDocFuncs):
        self._form_doc_funcs = form_doc_funcs
