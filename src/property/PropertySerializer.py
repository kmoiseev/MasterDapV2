from typing import List, Dict

from src.property.Property import Property


class PropertySerializer:

    @staticmethod
    def to_dict(props: List[Property]) -> Dict[str, str]:
        return {props[i].get_id(): props[i].get_val() for i in range(0, len(props))}
