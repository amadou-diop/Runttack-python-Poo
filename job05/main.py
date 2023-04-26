class Animal:
    def  __init__(self):
        self.age = 0
        self.prénom = ""
        
    def vieillir(self):
        self.age += 1
        
    animals = Animal()
    
    print("age initial de l'animal :", animals.age)
    
    animals.vieillir()
    print("age de lanimal après une année :", animals.age)
       
