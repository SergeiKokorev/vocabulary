import json
import os
import random


from translator import *



def main(src):

    files = []
    i = 0

    for file in os.listdir('myvoc'):
        path = os.path.join('myvoc', file)
        if os.path.isfile(path) and os.path.splitext(file)[1] == '.json':
            files.append([file, i])
            i += 1

    print('Choose vocabulari exercise: ')
    for file in files:
        print(f'\t{file[1]}: {file[0]}')
    
    ubung = input('File number: ')
    file = files[int(ubung)][0]

    with open(os.path.join('myvoc', file), 'r') as fp:
        words = json.load(fp)
    
    word_type = words.keys()
    
    for i, wt in enumerate(word_type):
        print(f'\t{i} : {wt}')
    
    wt = input('Please enter number of word type: ')
    k = list(word_type)[int(wt)]
    words = words[k]
    nw = len(words) - 1
    num_words = input('Please enter a number of words to learn: ')

    for i in range(1, int(num_words) + 1):

        index = random.randint(0, nw)
        
        k, m = (0, 1) if src == 'de' else (1, 0)

        tr = input(f'{i}) word is "{words[index][k]}": ')
        if tr.lower() == words[index][m].lower():
            print('\tOk')
        else:
            print(f'\tWrong. Right translation is "{words[index][m]}"')
        print()


if __name__ == "__main__":

    _exit = True
    src = ['de', 'en']

    while not _exit in ['n', 'N']:
    
        print('\t1: from de to en;\n\t2: from en to de')
        lang = input('Choose from which to which translate: ')
    
        main(src[int(lang) - 1])
        _exit = input('Another try (y/n): ')
