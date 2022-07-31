import json
import os.path


def load_json():
    try:
        with open('data/data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
        save_json(data)
    return data


def save_json(data):
    if not os.path.isdir('data'):
        os.mkdir('data')
    with open('data/data.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(data, ensure_ascii=False))