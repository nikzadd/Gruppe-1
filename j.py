from datetime import datetime
from f import lag_avtale
from g import avtale_tom

def liste_sjekk(avtale_tom, dato):
    liste_avtaler = []
    for avtale in avtale_tom:
        if avtale == dato:
            lag_avtale.tittel.append(liste_avtaler)
    return liste_avtaler