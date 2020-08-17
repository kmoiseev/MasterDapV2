from src.session.common.Session import Session


class SessionInMemory(Session):

    def __init__(self):
        pass

    def set_user_id(self, user_id: str):
        pass

    def get_user_id(self) -> str:
        pass

    def set_edit_doc_id(self, doc_id: str) -> str:
        pass

    def get_edit_doc_id(self) -> str:
        pass

    def set_form_doc_entity_id(self, entity_id: str):
        pass

    def get_form_doc_entity_id(self) -> str:
        pass
