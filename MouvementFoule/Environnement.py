from typing import List, Set, Dict, Tuple, Optional

from Grille import Grille

class Voyageur:
    def __init__(self, couleur: Tuple[int, int, int],
                 trajet: List[Porte], grille: Grille):
        self.couleur = couleur
        self.trajet = trajet
        self.grille = grille
        
    def seDeplacer(self) -> Tuple[int, int]:
        pass
    
class Obstacle:
    def __init__(self, couleur: Tuple[int, int, int], grille: Grille):
        self.couleur = couleur
        self.grille = grille

class Porte:
    def __init__(self, couleur: Tuple[int, int, int], grille: Grille):
        self.couleur = couleur
        self.grille = grille
        
