from datetime import datetime

# klasse for en avtale

class Avtale:
    def __init__(self, tittel, sted, starttidspunkt, varighet):
        self.tittel = tittel
        self.sted = sted
        self.starttidspunkt = starttidspunkt
        self.varighet = varighet
    def __str__(self):
        return 'Avtale ' +str(self.tittel)+'/'+str(self.sted)+'/'+int(self.starttidspunkt)+':'+int(self.varighet)


tittel = input("Skriv inn avtale")
sted = input("Vennligst skriv sted")
sted = str(sted)
starttidspunkt = input("Vennligst skriv starttidspunkt")
starttidspunkt = int(starttidspunkt)
varighet = input("Vennligst skriv inn varighet")
varighet = int(varighet)

DinAvtale = Avtale(tittel,sted,starttidspunkt,varighet)
print(DinAvtale)