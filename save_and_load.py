import json


def load_json():
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def save_json(data):
    with open('data.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(data, ensure_ascii=False))