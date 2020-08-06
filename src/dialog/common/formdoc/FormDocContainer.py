from src.dialog.common.Dialog import Dialog
from src.dialog.common.DialogContainer import DialogContainer
from src.dialog.common.DialogFactory import DialogFactory
from src.dialog.common.formdoc import FormDocFuncs


class FormDocContainer(DialogContainer, FormDocFuncs):

    def __init__(self, dialog_factory: DialogFactory):
        super().__init__(dialog_factory)

    def form_doc(self, form_doc_dialog_params):
        # todo
        pass

    def create_dialog(self) -> Dialog:
        return self.dialog_factory.create_form_doc_dialog(self)
