from datetime import datetime
from g import avtaler
from f import Avtale


def avtale_sjekk(dato, avtale_tom):
    liste_avtaler_samtidig = []
    for avtale in avtale_tom:
        if avtale.starttidspunkt == dato: #Avtale.startidspunkt
            liste_avtaler_samtidig.append(avtale)
    return liste_avtaler_samtidig

avtale_sjekk("dato", )


# if __name__ == "__main__":
#     avtale_liste = []
#     avtale_liste.append(lag_avtale())
#     avtaler(avtale_liste)
#     print(avtale_liste)
#     dato_sjekk = input("Sjekk dato: ")
#     dato_1 = datetime.fromisoformat(dato_sjekk)
#     avtale_sjekk(avtale_liste, dato_1)

