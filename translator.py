from deep_translator import GoogleTranslator as google


from const import DIACRITIC as diacritic


def translate(text: str, *, src: str='en', dest: str='ru'):

    translator = google()
    translator.source = src
    translator.target = dest
    result = translator.translate(text)
    return result
