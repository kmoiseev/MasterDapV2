from typing import Dict

from src.property.Property import Property


class Entity:

    def __init__(self, key: str, props: Dict[str, Property]):
        self.key = key
        self.props = props
