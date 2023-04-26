class Animal:
    def nommer(self, nom):
        self.prenom = nom

animals = Animal()

animals.nommer("Luna")
print("L'animal se nomme  :", animals.prenom)
