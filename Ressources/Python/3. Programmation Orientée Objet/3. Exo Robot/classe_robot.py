class Robot():
    directions =['Nord', 'Sud', 'Est', 'Ouest'] 
    deplacements = {'Nord':(1,0), 'Sud':(0,-1), 'Est':(1,0), 'Ouest':(-1,0)}
      
    
    def __init__(self, nom, position=(0,0),direction='Est'):
        self._nom = nom
        self.position = position
        self.direction = direction
        self.history = [position]
       

        
    # Methode pour avancer le robot 
    
    def avance(self):
        self.position = tuple(map(sum, zip(self.position, Robot.deplacements[self._direction])))
        self.history += [self.position, self.direction]
        return self
    
    
    # Methode de tourner à droite le robot 
    def droite(self):
        self._direction = Robot.directions[(Robot.directions.index(self._direction) + 1) %4]
        self.history = [self.position, self.direction]
        return self
        
    # Methode d'affichage du robot 
    def afficher(self , with_history=False):
        print(f""" Robot : {self._nom} 
                    est en position {self.position} 
                    orienté vers la direction {self.direction}
                    """)
        if with_history:
            print(f"après être passé par {self.direction}")
        

        

rbt = Robot('Thomaoc')
#rbt.avance().droite().afficher()
rbt.afficher(with_history=True)


