#from typing import List, Set, Dict, Tuple, Optional

from Environnement import Voyageur, Obstacle, Porte

class Grille:
    """ classe qui detremine la grille dans laquelle les voyageurs vont evoluer """
    def  __init__(self):
        self.voyageurs = dict()
        self.obstacles = dict()
        self.portes = dict()
        
    def addVoyageur(self, coord, v):
        pass
    
    def addObstacle(self, coords, m):
        pass
    
    def addPorte(self, coords, p):
        pass
    
    def getVoyageurs(self):
        pass
    
    def getObstacles(self) :
        pass
    
    def getPortes(self):
        pass
    
    def getPosition(self, v) :
        pass
    
    def setPosition(self, v, coord):
        pass
    
    def getContenuCase(self, coord) :
        pass
    
    def getDirection(self, v, p):
        pass
    
    def deleteVoyageur(self, v):
        pass
