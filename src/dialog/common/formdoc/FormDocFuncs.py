from abc import abstractmethod


class FormDocFuncs:

    @abstractmethod
    def form_doc(self, form_doc_dialog_params):
        pass

    @abstractmethod
    def get_form_doc_entity_id(self) -> str:
        pass

    @abstractmethod
    def closed_on_x(self):
        pass