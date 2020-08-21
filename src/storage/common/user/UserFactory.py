from typing import Dict

from src.property.PropertyFactory import PropertyFactory
from src.storage.common.user.User import User
from src.template.user.UserTemplate import UserTemplate


class UserFactory:

    def __init__(self, user_template: UserTemplate):
        self.user_template = user_template

    def create(self, key: str, props_values: Dict[str, str]) -> User:
        return User(
            key,
            PropertyFactory.create_from_template_and_dict(
                self.user_template.properties_templates,
                props_values,
                lambda prop_template_id: 'Property ' + prop_template_id + ' not found for user ' + key
            )
        )
