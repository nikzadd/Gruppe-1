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
    5: "Avlutte menyvalget",
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
        print("Takk og ha det bra")
        break
    else:
        print("Ugyldig valg, velg et nummer mellom 1 og 5:")
