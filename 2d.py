#c

class Kategori:
<<<<<<< Updated upstream
    def __init__(self, id = 1, navn=None, prioritet=None):
=======
    def __init__(self, id, navn, prioritet):
>>>>>>> Stashed changes
        self.id = id
        self.navn = navn
        self.prioritet = prioritet
        
    def __str__(self):
        return 'Kategori ' +str(self.id)+'/'+str(self.navn)+'/'+int(self.prioritet)
        
    
    def __str__ (self):
        return f"id: {self.id}, navn: {self.navn}, prioritet: {self.prioritet} "

#d

def lag_kategori():
    id = input("Skriv inn ID: ")
    navn = str(input("Skriv navn: "))
    prioritet = int(input("Skriv inn prioritet. Skriv på format: "))
    prioritet = i = 1
    Dinkategori = Kategori(id, navn, prioritet)
    return Dinkategori

if __name__ =="__main__":
    lag_kategori()
