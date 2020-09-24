from abc import abstractmethod


class FormDocFuncs:

    @abstractmethod
    def form_doc(self, form_doc_dialog_params):
        pass

    @abstractmethod
    def closed_on_x(self):
        pass