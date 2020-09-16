from typing import Dict

from src.property.Property import Property


class StringPropertyFormatter:

    def __init__(self, props: Dict[str, Property]):
        self.__props = {}
        for prop_key in props.keys():
            self.__props[prop_key] = props[prop_key].get_val()

    def format(self, string: str) -> str:
        return string.format_map(self.__props)
