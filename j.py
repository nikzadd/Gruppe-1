from datetime import datetime


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
