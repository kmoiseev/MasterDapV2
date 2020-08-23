from abc import abstractmethod


class Session:

    @abstractmethod
    def set_user_id(self, user_id: str):
        pass

    @abstractmethod
    def get_user_id(self) -> str:
        pass

    @abstractmethod
    def set_edit_entity_id(self, doc_id: str) -> str:
        pass

    @abstractmethod
    def get_edit_entity_id(self) -> str:
        pass

    @abstractmethod
    def set_form_doc_entity_id(self, entity_id: str):
        pass

    @abstractmethod
    def get_form_doc_entity_id(self) -> str:
        pass
