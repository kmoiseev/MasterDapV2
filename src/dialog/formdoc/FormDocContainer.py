from src.dialog.Dialog import Dialog
from src.dialog.DialogContainer import DialogContainer
from src.dialog.DialogFactory import DialogFactory
from src.dialog.formdoc.FormDocFuncs import FormDocFuncs


class FormDocContainer(DialogContainer, FormDocFuncs):

    def __init__(self, dialog_factory: DialogFactory):
        super().__init__(dialog_factory)

    def form_doc(self, form_doc_dialog_params):
        # todo
        pass

    def create_dialog(self) -> Dialog:
        return self.dialog_factory.create_form_doc_dialog(self)
