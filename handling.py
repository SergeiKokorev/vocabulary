from tools import write_json, update_json


if __name__ == "__main__":

    words = [
        ('berichten', 'verbenen'), ('besichtigen', 'verben'), ('bestehen', 'verben'),
        ('erfinden', 'verben'), ('fliesen', 'verben'), ('gehoren', 'verben'),
        ('wachsen', 'verben'), ('wahlen', 'verben'), ('wandern', 'verben'),
        ('der Bach', 'nomen'), ('der Bau', 'nomen'), ('der Berg', 'nomen'),
        ('die Brucke', 'nomen'), ('das Datum', 'nomen'), ('das Denkmal', 'nomen'),
        ('das Elektrogerat', 'nomen'), ('das Ende', 'nomen'), ('der Fluss', 'nomen'),
        ('das Gasthaus', 'nomen'), ('das Gebiet', 'nomen'), ('die Grenze', 'nomen'),
        ('der Hafen', 'nomen'), ('die Kneipe', 'nomen'), ('die Kuste', 'nomen'),
        ('Lebensmittel', 'nomen'), ('die Nation', 'nomen'), ('die Pension', 'nomen'),
        ('die Ruine', 'nomen'), ('die Schriftstellerin', 'nomen'), ('die Sehenswurdig', 'nomen'),
        ('der Sitz', 'nomen'), ('die Sprache', 'nomen'), ('der Staat', 'nomen'),
        ('der Tod', 'nomen'), ('das Werk', 'nomen'), ('das Zentrum', 'nomen'),
        ('endgultig', 'adjektive'), ('fertig', 'adjektive'), ('offiziell', 'adjektive'),
        ('tief', 'adjektive'), ('damals', 'adverbien'), ('daher', 'adverbien'),
        ('Passen Sie auf', 'ausdrucke')
    ]
    write_json('kapitel10.json', words)   
