import json
import os
import random

from datetime import date


from translator import *


def get_files(dir):

    files = []

    for file in os.listdir(dir):
        path = os.path.join(dir, file)
        if os.path.isfile(path) and os.path.splitext(file)[1] == '.json':
            files.append(file)

    return files


def main(src, dest, exercise, num_words):

    with open(exercise, 'r') as fp:
        
        vocab = json.load(fp)
        print('Enter you translation for word:')
        wrong, right = 0, 0

        for i in range(1, num_words+1):
            w = random.randint(0, len(vocab) - 1)
            word = vocab[w][src]
            trans = vocab[w][dest]
            type = vocab[w]['type']
            dt = vocab[w]['date']
            rate = vocab[w]['rate']

            translation = input(f'\t{i}) {word} ({type}), last time {dt}, rate: {rate}: ')

            if translation.lower() == trans.lower():
                print('\t\tRight')
                vocab[w]['date'] = date.today().isoformat()
                right += 1
                if rate < 10: vocab[w]['rate'] = rate + 1
            else:
                print(f'\t\tWrong, right translation is {trans}')
                if rate: vocab[w]['rate'] -= 1
                wrong += 1

    print(f'Right answers {right}. Wrong answers {wrong}. {right* 100 / num_words} % of right answers.')

    with open(exercise, 'w', newline='') as fp:
        json.dump(vocab, fp, indent=3)


if __name__ == "__main__":

    _exit = True
    lang = ["en", "de"]
    directory = 'myvoc'

    while not _exit in ['n', 'N']:

        src = input(f'Enter source {str(lang)[1:-1]}: ')
        dest = input(f'Enter destanation: {str(lang)[1:-1]}: ')
        files = get_files(directory)

        for i, file in enumerate(files, 1):
            print(f'\t{i}) {file}')

        file = int(input('Enter file (exercise) number: '))
        num_words = int(input('Enter number of words to translate: '))

        main(src=src,
             dest=dest,
             exercise=os.path.join(directory, files[file-1]),
             num_words=num_words)
        _exit = input('Another try (y/n): ')
