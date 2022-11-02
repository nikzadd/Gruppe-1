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

<<<<<<< HEAD
#Hent fra avtalefil
from f import lag_avtale

def liste_sjekk(liste_avtaler, dato):
    liste_avtaler = []
    with open("avtalefil.txt", "r", encoding="UTF8") as avtalefil:
        for linje in avtalefil:
            if dato == dato:
                linje.append = liste_avtaler
    return liste_avtaler

#test
if __name__ == "__main__":
    dato = input("Skriv inn dato på formen YYYY-MM-DD XX:XX:XX: ")
    #dato = datetime.fromisoformat(dato_sjekk)
    test = liste_sjekk(liste_sjekk, dato)
    print(test)
=======
# if __name__ == "__main__":
#     avtale_liste = []
#     avtale_liste.append(lag_avtale())
#     avtaler(avtale_liste)
#     print(avtale_liste)
#     dato_sjekk = input("Sjekk dato: ")
#     dato_1 = datetime.fromisoformat(dato_sjekk)
#     avtale_sjekk(avtale_liste, dato_1)
>>>>>>> 78e79ee672a8a14e0d60d4d88223aa4b134e60b2
