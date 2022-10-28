from h import avtale_til_tekstfil
from f import lag_avtale
from g import avtaler
from i import lesing_av_fil

liste_med_avtaler = []


meny_valg = {
    1: "Lese inn avtaler fra fil",
    2: "Skrive avtale til fil",
    3: "Skrive inn en ny avtale",
    4: "Skrive ut alle avtalene",
    5: "Slette en avtale",
    6: "Redigere en avtale",
    7: "Avslutte"
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

def valg5():
    valget = int(input("Hvilken avtale vil du fjerne? Skriv nummeret til avtalen: ") + 1)
    try:
        liste_med_avtaler.remove(valget)
    except ValueError:
        pass
    print("Da fjernet du avtale nummer", valget)

#def valg6():


while(True):
    print_meny()
    valg = ""
    try:
        valg = input("Hva ønsker du å gjøre?: ")
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
        print("Takk og ha det bra")
        break
    else:
        print("Ugyldig valg, velg et nummer mellom 1 og 5:")
