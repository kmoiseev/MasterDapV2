from typing import List, Dict

from src.docs_publisher.common.DocsPublisher import DocsPublisher
from src.property.Property import Property


class DocsPublisherDocx(DocsPublisher):

    def publish_docs(self, entity_props: Dict[str, Property], form_doc_filled_props: Dict[str, Property]):
        props: Dict[str, Property] = entity_props.copy()
        props.update(form_doc_filled_props)
        print('HEEEEY')
