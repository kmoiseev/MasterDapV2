from src.util.json.JsonReader import JsonReader


class PropertyTypeConfig:

    def __init__(self, property_type_config_folder):
        self.dropdowns = JsonReader(property_type_config_folder + 'dropdowns.json').read()["dropdowns"]
