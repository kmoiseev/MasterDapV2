import json


def read_json(file_path: str):
    file_pointer = open(file_path, 'r', encoding='utf-8')
    json_parsed = json.load(file_pointer)
    file_pointer.close()
    return json_parsed


def write_json(file_path: str, json_data: dict):
    file_pointer = open(file_path, 'w', encoding='utf-8')
    file_pointer.write(str(json.dumps(json_data, ensure_ascii=False, sort_keys=True, indent=4)))
    file_pointer.close()
