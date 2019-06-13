from typing import List, Set, Dict, Tuple, Optional

from Environnement import Voyageur, Obstacle, Porte

class Grille:
    def  __init__(self):
        self.voyageurs: Dict[Tuple[int, int], Voyageur] = dict()
        self.obstacles: Dict[Tuple[int, int], Obstacle] = dict()
        self.portes: Dict[Tuple[int, int], Porte] = dict()
        
    def addVoyageur(self, coord: Tuple[int, int], v: Voyageur):
        pass
    
    def addObstacle(self, coords: List[Tuple[int, int]], m: Obstacle):
        pass
    
    def addPorte(self, coords: List[Tuple[int, int]], p: Porte):
        pass
    
    def getVoyageurs(self) -> Dict[Tuple[int, int], Voyageur]:
        pass
    
    def getObstacles(self) -> Dict[Tuple[int, int], Obstacle]:
        pass
    
    def getPortes(self) -> Dict[Tuple[int, int], Porte]:
        pass
    
    def getPosition(self, v: Voyageur) -> Tuple[int, int]:
        pass
    
    def setPosition(self, v: Voyageur, coord: Tuple[int, int]):
        pass
    
    def getContenuCase(self, coord: Tuple[int, int]) -> Tuple[Optional[Voyageur], Optional[Obstacle], Optional[Porte]]:
        pass
    
    def getDirection(self, v: Voyageur, p: Porte) -> Tuple[int, int]:
        pass
    
    def deleteVoyageur(self, v: Voyageur):
        pass
