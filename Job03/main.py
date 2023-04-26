"""class Operation:
    def  __init__(self, nombre1 , nombre2):
        self.nombre1 = 12
        self.nombre2 = 3
        self.append()
        
    def show(self):
        print("nombre1:" , self. nombre1)
        print("nombre2:" , self. nombre2)
        print(append)
        
Operation = Operation(12, 3)
Operation.show()
"""""

"""class Operation:

    
    def  __init__(self, nombre1, nombre2):
        self.nombre1 = 25
        self.nombre2 = 30
        
    def __add__(self):
        return Addition (self.nombre1 + self.nombre2)
        
    
        """




class Personne(object):     
       
    # Constructeur         
    def __init__(self, nom, cin):    
        self.nom = nom 
        self.cin = cin 
 
    def afficher(self): 
        print("Nom : ",self.nom) 
        print("CIN : ",self.cin) 
 
 
# création d'une variable d'instance
p=Personne("ISMAIL", "EE456788")
 
# appeler une fonction de la classe Personne en utilisant son instance
p.affiche()