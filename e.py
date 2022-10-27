from datetime import datetime

# d

class Avtale:
    def __init__(self, tittel, sted, starttidspunkt, varighet):
        self.tittel = tittel
        self.sted = sted
        self.starttidspunkt = starttidspunkt
        self.varighet = varighet
    

tittel = input("Skriv inn avtale")
sted = input("Vennligst skriv sted")
sted = str(sted)
starttidspunkt = input("Vennligst skriv starttidspunkt")
starttidspunkt = datetime(starttidspunkt)
varighet = input("Vennligst skriv inn varighet")
verighet = int(varighet)

DinAvtale = Avtale(tittel,sted,starttidspunkt,varighet)
print(DinAvtale)

#e

def __str__(self):
      return "(%s, %s, %s)" % (self._n, self._p, self._b)

#eller

def __str__(self):
        return 'Avtale ' +str(self.tittel)+'/'+str(self.sted)+'/'+datetime(self.starttidspunkt)+':'+int(self.varighet)

