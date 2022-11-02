from datetime import datetime
from f import lag_avtale
from e import Avtale

def avtale_sjekk(avtale_liste, dato):
    liste_avtaler_samtidig = []
    for avtale in avtale_liste:
        if avtale == Avtale.starttidspunkt: #Avtale.startidspunkt
            if avtale == dato:
                Avtale.tittel.append(liste_avtaler_samtidig)
    return liste_avtaler_samtidig

# if __name__ == "__main__":
#     avtale_liste = []
#     avtale_liste.append(lag_avtale())
#     avtaler(avtale_liste)
#     print(avtale_liste)
#     dato_sjekk = input("Sjekk dato: ")
#     dato_1 = datetime.fromisoformat(dato_sjekk)
#     avtale_sjekk(avtale_liste, dato_1)
