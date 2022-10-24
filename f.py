from datetime import datetime

# d

class Avtale:
    def __init__(self, tittel, sted, starttidspunkt, varighet):
        self.tittel = tittel
        self.sted = sted
        self.starttidspunkt = starttidspunkt
        self.varighet = varighet
    
    #e metode som returnerer en streng som kan skrives

    def __str__(self):
        return Avtale  +str(self.tittel)+'/'+str(self.sted)+'/'+datetime(self.starttidspunkt)+':'+int(self.varighet)

#f
tittel = input("Skriv inn hva avtalen gjelder ")
sted = input("Skriv sted ")
sted = str(sted)
starttidspunkt = input("Skriv starttidspunkt ")
starttidspunkt = datetime(starttidspunkt)
varighet = input("Skriv varighet på avtalen ")
varighet = int(varighet)



DinAvtale = Avtale(tittel,sted,starttidspunkt,varighet)
print(DinAvtale)

