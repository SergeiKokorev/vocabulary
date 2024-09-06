import os


from typing import Sequence
from datetime import date
from json import dump, load
from translator import translate


def touch(path):
    with open(path, 'a') as f:
        os.utime(path, None)


def get_json_dump(words: Sequence[tuple]) -> Sequence[dict]:

    now = date.today().isoformat()
    json_dump = []
    keys = ('de', 'en', 'type', 'date', 'rate')

    for word in words:
        values = (word[0], translate(word[0], src='de', dest='en'), word[1], now, 0)
        json_dump.append(dict([(k, v) for k, v in zip(keys, values)]))

    return json_dump


def write_json(file_name: str, words: Sequence[tuple]) -> None:

    json_dump = get_json_dump(words)

    try:
        with open(file_name, 'w', newline='') as fp:
            dump(json_dump, fp, indent=2)
    except PermissionError:
        raise PermissionError(f'You do not have permission to write file {file_name}')


def update_json(file_name: str, words: Sequence[tuple]):

    words_dict = None

    try:
        with open(file_name, 'r') as fp:
            words_dict = load(fp)
    except FileExistsError:
        raise FileExistsError(f'file {file_name} does not exist')

    if not words_dict:
        return None
    
    new_words = get_json_dump(words)
    words_dict.append(new_words)

    try:
        with open(file_name, 'w', newline='') as fp:
            dump(words_dict, fp, indent=2)
    except PermissionError:
        raise PermissionError(f'You do not have access to file {file_name}')
