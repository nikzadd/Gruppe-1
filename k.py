from f import lag_avtale
from h import avtale_til_tekstfil

def finn_en_streng():
    nokkelord=str(input("Skriv nøkkelord eller setning i en avtale"))
    with open("avtalefil.txt",'r',encoding="UTF8") as nokkelord_open:
        linjer=nokkelord_open.readlines()
        for linje in linjer:
            if linje.find(nokkelord) != -1:
                print("Avtalenummer:",linjer.index(linje)+1, linje)
finn_en_streng()













