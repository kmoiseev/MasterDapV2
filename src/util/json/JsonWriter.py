import json


class JsonWriter:

    def __init__(self, file_path: str, json_data: dict):
        self.file_path = file_path
        self.json_data = json_data

    def write(self):
        file_pointer = open(self.file_path, 'w', encoding='utf-8')
        file_pointer.write(str(json.dumps(self.json_data, ensure_ascii=False, sort_keys=True, indent=4)))
        file_pointer.close()