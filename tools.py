import os
import json

from translator import translate


def touch(path):
    with open(path, 'a') as f:
        os.utime(path, None)


def add_word(word, translation, type, file):

    aw = 'r+' if os.path.exists(file) else 'w'

    with open(file, aw, newline='') as f:

        if os.path.getsize(file) > 0:
            f.seek(0)
            data = json.load(f)
        else:
            data = {}
            data[type] = []

        data[type].append((word, translation))
        json.dump(data, f, indent=2)


def add_words(words, translations, type, file):

    res = dict([(type, [])])

    if not os.path.exists(file): 
        touch(file)

    if not os.path.getsize(file) > 0:
        data = {}
    else:
        with open(file, 'r') as f:
            data = json.load(f)

    with open(file, 'w', newline='') as f:

        for word, tr in zip(words, translations):
            res[type].append((word, tr))

        data.update(res)
        json.dump(data, f, indent=3)


if __name__ == "__main__":

    file = os.path.join('myvoc', 'kapitel7.json')
    translations = []

    # Fill lists below to translate german words to english and write them to the file
    verben = []
    nomen = []
    adjektive = []
    adverben = []

    for word in verben:
        translations.append(translate(word, src='de', dest='en'))
    add_words(verben, translations, 'verben', file)

    translations = []
    for word in nomen:
        translations.append(translate(word, src='de', dest='en'))
    add_words(nomen, translations, 'nomen', file)

    translations = []
    for word in adjektive:
        translations.append(translate(word, src='de', dest='en'))

    add_words(adjektive, translations, 'adjektive', file)

    translations = []
    for word in adverben:
        translations.append(translate(word, src='de', dest='en'))

    add_words(adverben, translations, 'adjektive', file)
