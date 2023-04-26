class  Personne:
    def  __init__(self, nom, prénom):
        self.nom = nom
        self.prénom = prénom
        
    def sePresenter(self):
        return f" Je m'appelle { self.nom} {self.prénom}."
        
personne1 = Personne("DIOP", "Amadou")
personne2 = Personne("NGAIDO", "Ramatoulaye")
personne3 = Personne("BA", "Abdoulaye")

print(personne1.sePresenter())
print(personne2.sePresenter())
print(personne3.sePresenter())
        
    