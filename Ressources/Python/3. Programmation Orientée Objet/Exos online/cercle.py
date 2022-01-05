
from math import *


class Cercle:
    def __init__(self, a, b, r):
        self.a = a
        self.b = b
        self.r = r
        
    
        # Methode de calcul de la surface du cercle 
    
        def surface(self):
            return self.r**2*pi
           
         # Methode de calcul de la surface du cercle 
    
        def perimetre(self):
            return self.r * 2*pi
        
        
        #Methode d'appartence au cercle vérifie l'Equation cartesienne du cercle est verifiée =>(x-a)² + (y-b)² == r²
        
        def testAppartenance(self, x, y):
            if ((x - self.a)**2 + (y-self.b**2) == self.r**2):
                print(f"Le point de coordonnées: {x,y} appartient au cercle")
            else:
                print(f"Le point de coordonnées: {x,y} n'appartient pas au cercle")


c1 = Cercle(2,4,3)
c1.surface()
c1.perimetre()
c1.testAppartenance(1,3)