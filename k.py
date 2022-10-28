from f import lag_avtale
from h import avtale_til_tekstfil




def finn_en_streng():
    nokkelord=str(input("Skriv nøkkelord eller setning i en avtale"))
    try:
        nokkelord_open = open("avatalefil.txt", "r", encoding="UTC8")
        for i in range(len(avtaleliste)):
            str(nokkelord_open.find(nokkelord))
    except:
        pass

finn_en_streng()



