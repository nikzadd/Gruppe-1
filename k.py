from f import lag_avtale
from h import avtale_til_tekstfil
from i import lesing_av_fil
from j import liste_avtaler



def finn_en_streng():
    nokkelord=str(input("Skriv nøkkelord eller setning i en avtale"))
    try:
        for i in range(len(avtaleliste)):
            avtalefil.find(nokkelord)
            nokkelord_open=open("avatalefil.txt","r",encoding="UTC8")
    except:
        pass
