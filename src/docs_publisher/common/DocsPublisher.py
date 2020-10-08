from abc import abstractmethod
from typing import List, Dict

from src.property.Property import Property


class DocsPublisher:

    @abstractmethod
    def publish_docs(self, entity_props: Dict[str, Property], form_doc_filled_props: Dict[str, Property]):
        pass
