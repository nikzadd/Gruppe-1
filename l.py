from h import avtale_til_tekstfil
from f import lag_avtale
from g import avtaler
from i import lesing_av_fil
from datetime import datetime

liste_med_avtaler = []

meny_valg = {
    1: "Lese inn avtaler fra fil",
    2: "Skrive avtale til fil",
    3: "Skrive inn en ny avtale",
    4: "Skrive ut alle avtalene",
    5: "Slette en avtale",
    6: "Redigere en avtale",
    7: "Avslutte",
    8: "Sjekke samme dato"
}

def print_meny():
    for valget in meny_valg.keys():
        print (valget, "--", meny_valg[valget] )

def valg1():
    lesing_av_fil()
def valg2():
     avtale_til_tekstfil(liste_med_avtaler)

def valg3():
     liste_med_avtaler.append(lag_avtale())

def valg4():
    avtaler(liste_med_avtaler)

#m

def valg5():
    valget = int(input("Hvilken avtale vil du fjerne? Skriv nummeret til avtalen: "))
    try:
        liste_med_avtaler.pop(valget-1)
        avtale_til_tekstfil(liste_med_avtaler)
    except ValueError:
        print("Oisann! Det gikk ikke")
    print("Da fjernet du avtale nummer", valget)

#n

def valg6():
    rediger_valg = int(input("Hvilken avtale vil du redigere? Skriv nummeret til avtalen: "))
    try:
        liste_med_avtaler.pop(rediger_valg-1)
        avtale_til_tekstfil(liste_med_avtaler)
        valg3()
        
    except ValueError:
        pass

def avtale_sjekk(dato, avtale_tom):
    liste_avtaler_samtidig = []
    for avtale in avtale_tom:
        if avtale.starttidspunkt == dato: #Avtale.startidspunkt
            liste_avtaler_samtidig.append(avtale.tittel)
    return liste_avtaler_samtidig

while(True):
    print_meny()
    valg = ""
    try:
        valg = int(input("Hva ønsker du å gjøre?: "))
    except ValueError:
        print("Feil inntasting, velg et nummer:")
    
    if valg == 1:
        valg1()
    elif valg == 2:
        valg2()
    elif valg == 3:
        valg3()
    elif valg == 4:
        valg4()
    elif valg == 5:
        valg5()
    elif valg == 6:
        valg6()
    elif valg == 7:
        print("Takk og ha det bra!")
        break
    elif valg == 8:
        datoen = (input("Skriv inn en dato på datetime-format:"))
        datetimedato = datetime.fromisoformat(datoen)
        print(avtale_sjekk(datetimedato, liste_med_avtaler))
    else:
        print("Ugyldig valg, velg et nummer mellom 1 og 5:")
