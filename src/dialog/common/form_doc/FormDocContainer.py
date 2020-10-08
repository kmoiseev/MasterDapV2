from typing import List

from src.dialog.common.Dialog import Dialog
from src.dialog.common.DialogContainer import DialogContainer
from src.dialog.common.DialogFactory import DialogFactory
from src.dialog.common.form_doc.FormDocFuncs import FormDocFuncs
from src.docs_publisher.common.DocsPublisher import DocsPublisher
from src.property.Property import Property
from src.session.common.Session import Session
from src.storage.common.entity.EntityStorage import EntityStorage
from src.template.doc.DocTemplate import DocTemplate
from src.template.doc.DocsTemplates import DocsTemplates
from src.template.property.PropertyTemplate import PropertyTemplate


class FormDocContainer(DialogContainer, FormDocFuncs):

    def __init__(
            self,
            dialog_factory: DialogFactory,
            session: Session,
            docs_publisher: DocsPublisher,
            storage: EntityStorage,
            docs_templates: DocsTemplates
    ):
        super().__init__(dialog_factory)
        self.__session = session
        self.__docs_publisher = docs_publisher
        self.__storage = storage
        self.__docs_templates = docs_templates

    def form_doc(self, form_doc_filled_props: List[Property]):
        self.__docs_publisher.publish_docs(
            self.__storage.get_entity(
                self.__session.get_form_doc_entity_key()
            ).props,
            {
                form_doc_filled_props[i].get_id(): form_doc_filled_props[i]
                for i in range(0, len(form_doc_filled_props))
            }
        )

    def get_docs_templates(self) -> List[DocTemplate]:
        return self.__docs_templates.templates

    def get_form_doc_entity_key(self) -> str:
        return self.__session.get_form_doc_entity_key()

    def create_dialog(self) -> Dialog:
        return self.dialog_factory.create_form_doc_dialog(self)

    def closed_on_x(self):
        self.close_dialog()
