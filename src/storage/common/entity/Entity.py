from typing import List

from src.property.Property import Property


class Entity:

    def __init__(self, key: str, props: List[Property]):
        self.key = key
        self.props = props
