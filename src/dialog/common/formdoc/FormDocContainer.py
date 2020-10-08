from src.dialog.common.Dialog import Dialog
from src.dialog.common.DialogContainer import DialogContainer
from src.dialog.common.DialogFactory import DialogFactory
from src.dialog.common.formdoc.FormDocFuncs import FormDocFuncs
from src.session.common.Session import Session
from src.storage.common.entity.EntityStorage import EntityStorage


class FormDocContainer(DialogContainer, FormDocFuncs):

    def __init__(self, dialog_factory: DialogFactory, session: Session):
        super().__init__(dialog_factory)
        self.__session = session

    def form_doc(self, form_doc_dialog_params):
        # todo
        pass

    def get_form_doc_entity_id(self) -> str:
        return self.__session.get_form_doc_entity_id()

    def create_dialog(self) -> Dialog:
        return self.dialog_factory.create_form_doc_dialog(self)

    def closed_on_x(self):
        self.close_dialog()
