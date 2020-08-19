import json


class JsonReader:

    def __init__(self, file_path: str):
        self.file_path = file_path

    def read(self):
        file_pointer = open(self.file_path, 'r', encoding='utf-8')
        json_parsed = json.load(file_pointer)
        file_pointer.close()
        return json_parsed
