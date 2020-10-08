from abc import abstractmethod

from src.dialog.common.manage_entity.ManageEntityDialogMode import ManageEntityDialogMode


class Session:

    @abstractmethod
    def set_user_id(self, user_id: str):
        pass

    @abstractmethod
    def get_user_id(self) -> str:
        pass

    @abstractmethod
    def set_edit_entity_id(self, entity_id: str):
        pass

    @abstractmethod
    def get_edit_entity_key(self) -> str:
        pass

    @abstractmethod
    def set_manage_entity_mode(self, mode: ManageEntityDialogMode):
        pass

    @abstractmethod
    def get_manage_entity_mode(self) -> ManageEntityDialogMode:
        pass

    @abstractmethod
    def set_form_doc_entity_key(self, entity_id: str):
        pass

    @abstractmethod
    def get_form_doc_entity_key(self) -> str:
        pass
