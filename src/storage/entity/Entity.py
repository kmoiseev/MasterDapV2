from typing import Dict


class Entity:

    def __init__(self, key: str, props: Dict[str, str]):
        self.key = key
        self.props = props
