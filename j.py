import datetime
from g import avtale_tom
from datetime import datetime



def liste_avtaler(avtale_tom, dato):
    liste_avtaler = []
    for i in avtale_tom:
        if dato == avtale_tom[2]:
            avtale_tom[0].append = liste_avtaler
    return liste_avtaler

#test
if __name__ == "__main__":
    dato_sjekk = input("Skriv inn dato: ")
    dato = datetime.fromisoformat(dato_sjekk)
    test = liste_avtaler(avtale_tom, dato)
    print(test)

