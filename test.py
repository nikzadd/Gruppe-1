meny_valg = {
    1: "lese inn avtaler fra fil",
    2: "skrive avtale til fil",
    3: "skrive inn en ny avtale",
    4: "skrive ut alle avtalene",
    5: "avlutte menyvalge",
}

def print_meny():
    for valget in meny_valg.keys():
        print (valget, '--', meny_valg[valget] )

def valg1():
     print("her er valg1")

def valg2():
     print("her er valg2")

def valg3():
     print("her er valg3")

def valg4():
    print("her er valg 4")


while(True):
    print_meny()
    valg = ""
    try:
        valg = int(input("hva ønsker du å gjøre: "))
    except:
        print("feil inntasting, velg et nummer:")
    
    if valg == 1:
        valg1()
    elif valg == 2:
        valg2()
    elif valg == 3:
        valg3()
    elif valg == 4:
        valg4()
    elif valg == 5:
        print("takk og hade bra")
        break
    #else:
        #print("ugyldig valg, velg ett nummer mellom 1 og 5:")