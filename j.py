from datetime import datetime


#Hent fra avtalefil

def liste_avtaler(liste_avtaler, dato):
    liste_avtaler = []
    with open("avtalefil.txt", "r", encoding="UTF8") as avtalefil:
        for j in avtalefil:
            if dato == avtalefil[3]:
                avtalefil[1].append = liste_avtaler
    return liste_avtaler

#test
if __name__ == "__main__":
    dato_sjekk = input("Skriv inn dato: ")
    dato = datetime.fromisoformat(dato_sjekk)
    test = liste_avtaler(liste_avtaler, dato)
    print(test)
