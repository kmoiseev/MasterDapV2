from src.dialog.common.manage_entity.ManageEntityDialogMode import ManageEntityDialogMode
from src.session.common.Session import Session


class SessionInMemory(Session):

    def __init__(self):
        self.user_id = ''
        self.doc_id = ''
        self.edit_entity_id = ''
        self.form_doc_entity_id = ''
        self.manage_entity_mode = ManageEntityDialogMode.NONE


    def set_user_id(self, user_id: str):
        self.user_id = user_id

    def get_user_id(self) -> str:
        return self.user_id

    def set_edit_entity_id(self, entity_id: str):
        self.edit_entity_id = entity_id

    def get_edit_entity_key(self) -> str:
        return self.edit_entity_id

    def set_manage_entity_mode(self, mode: ManageEntityDialogMode):
        self.manage_entity_mode = mode

    def get_manage_entity_mode(self) -> ManageEntityDialogMode:
        return self.manage_entity_mode

    def set_form_doc_entity_key(self, entity_id: str):
        self.form_doc_entity_id = entity_id

    def get_form_doc_entity_key(self) -> str:
        return self.form_doc_entity_id


