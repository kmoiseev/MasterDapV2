from abc import abstractmethod
from typing import List

from src.property.Property import Property
from src.template.doc.DocTemplate import DocTemplate


class FormDocFuncs:

    @abstractmethod
    def form_doc(self, form_doc_filled_props: List[Property]):
        pass

    @abstractmethod
    def get_form_doc_entity_key(self) -> str:
        pass

    @abstractmethod
    def get_docs_templates(self) -> List[DocTemplate]:
        pass

    @abstractmethod
    def closed_on_x(self):
        pass
