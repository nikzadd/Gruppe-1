

meny = {}
meny["1"]= "les inn avtaler fra fil."
meny["2"]= "skrive avtale til fil."
meny["3"]= "skrive inn en ny avtale."
meny["4"]= "skrive ut alle avtalene."
meny["5"]= "Avslutt"

while True: 
  options=meny.keys()
  options.sort()
    for entry in options: 
        print entry, menu[entry]

    svar = input("Hva ønsker du å gjøre?")
    if svar == "1":
        print("gjort")
    elif svar == "2":
        print("gjort")
    elif svar == "3":
        print("gjort")
    elif svar == "4":
        print("gjort")
    elif svar == "5":
        break






