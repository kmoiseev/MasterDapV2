import logging
from typing import Callable, Dict, List

from src.property.Property import Property
from src.property.PropertyValue import PropertyValue
from src.template.property.PropertyTemplate import PropertyTemplate


class PropertyFactory:

    @staticmethod
    def create_from_template_and_dict(
            props_templates: List[PropertyTemplate],
            props_values: Dict[str, str],
            prop_not_found_callback: Callable[[str], str]
    ) -> Dict[str, Property]:
        res_props: Dict[str, Property] = {}

        for property_template in props_templates:
            prop_template_id = property_template.id
            if prop_template_id in props_values:
                res_props[prop_template_id] = \
                    Property(property_template, PropertyValue(props_values[prop_template_id]))
            else:
                logging.error(prop_not_found_callback(prop_template_id))

        return res_props
