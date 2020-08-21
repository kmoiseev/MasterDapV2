from typing import Dict

from src.property.Property import Property


class EntitySerializer:

    @staticmethod
    def serialize(props: Dict[str, Property]) -> Dict[str, str]:
        return {props[i].get_id(): props[i].get_val() for i in props.keys()}
