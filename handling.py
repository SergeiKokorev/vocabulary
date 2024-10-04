from os.path import join
from tools import write_json, update_json


if __name__ == "__main__":

    words = [
        ('andern', 'verben'), ('ansehen', 'verben'), ('anziehen', 'verben'), ('argern', 'verben'),
        ('aussehen', 'verben'), ('finden', 'verben'), ('gefallen', 'verben'), ('gehoren zu', 'verben'),
        ('kritisieren', 'verben'), ('kundigen', 'verben'), ('lugen', 'verben'), ('sich vorstellen', 'verben'),
        ('zahlen', 'verben'), ('der Angestellte', 'nomen'), ('der Anzug', 'nomen'), 
        ('der Arbeitgeber', 'nomen'), ('der Arbeitsamt', 'nomen'), ('das Auge', 'nomen'),
        ('das Badezimmer', 'nomen'), ('der Bauch', 'nomen'), ('die Bluse', 'nomen'), ('die Brille', 'nomen'),
        ('das Ergebnis', 'nomen'), ('der Feind', 'nomen'), ('das Gesicht', 'nomen'), ('dsa Haar', 'nomen'),
        ('der Hals', 'nomen'), ('das Hemd', 'nomen'), ('die Hochzeit', 'nomen'), ('die Hose', 'nomen'),
        ('die Krawatte', 'nomen'), ('die Leistung', 'nomen'), ('die Liebe', 'nomen'),
        ('die Meinung', 'nomen'), ('der mund', 'nomen'), ('der Musiker', 'nomen'), ('der Prozess', 'nomen'),
        ('der Punkt', 'nomen'), ('der Rechtsanwalt', 'nomen'), ('die Stelle', 'nomen'),
        ('die Strickjacke', 'nomen'), ('der Strumpf', 'nomen'), ('der Test', 'nomen'),
        ('das Vorurteil', 'nomen'), ('angenehm', 'dajektive'), ('arm', 'adjektive'), ('ahnlich', 'adjektive'),
        ('dick', 'adjektive'), ('dunn', 'adjektive'), ('dumm', 'adjektive'), ('ehrlich', 'adjektive'),
        ('gefahrlich', 'adjektive'), ('gemutlich', 'adjektive'), ('hasslich', 'adjektive'),
        ('klug', 'adjektive'), ('komisch', 'adjektive'), ('konservativ', 'adjektive'),
        ('offen', 'adjektive'), ('punktlich', 'adjektive'), ('rund', 'adjektive'), ('schlank', 'adjektive'),
        ('schmal', 'adjektive'), ('treu', 'adjektive'), ('verruckt', 'adjektive'), ('weich', 'adjektive'),
        ('bestimmt', 'adverbien'), ('etwa', 'adverbien'), ('meinetwegen', 'adverbien'),
        ('meistens', 'adverbien'), ('sonst', 'adverbien'), ('weiter', 'adverbien'), ('ziemlich', 'adverbien'),
    ]
    write_json(join('myvoc', 'kapitel2_1.json'), words)   
