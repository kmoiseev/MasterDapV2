from typing import Dict

from src.property.Property import Property


class User:
    def __init__(self, key, props: Dict[str, Property]):
        self.key = key
        self.props = props
