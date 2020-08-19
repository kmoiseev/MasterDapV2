import logging
from typing import List, Dict

from src.property.Property import Property
from src.property.PropertyValue import PropertyValue
from src.storage.common.user.User import User
from src.template.user.UserTemplate import UserTemplate


class UserFactory:

    def __init__(self, user_template: UserTemplate):
        self.user_template = user_template

    def create(self, key: str, props_values: Dict[str, str]) -> User:

        res_props: Dict[str, Property] = {}

        for property_template in self.user_template.properties_templates:
            prop_template_id = property_template.id
            if prop_template_id in props_values:
                res_props[prop_template_id] = \
                    Property(property_template, PropertyValue(props_values[prop_template_id]))
            else:
                logging.error('Property ' + prop_template_id + ' not found for user ' + key)

        return User(key, res_props)
