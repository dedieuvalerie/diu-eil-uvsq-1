#from typing import List, Set, Dict, Tuple, Optional

from Grille import Grille

class Voyageur :
    """ cree et determine un voyageur ; attributs : une couleur (tuple de 3 entiers) et une liste trajet contenant les
    coordonnees des differentes etapes pour arriver a la porte finale (tuples de deux entiers) ; cette liste est mise a jour au fur et a mesure
    que les etapes sont franchies ; lorsqu'elle est vide, le voyageur a atteint son but. Ce voyageur appartient a une grille
    (dictionnaire) """
    
    def __init__(self, couleur,trajet, grille):
        self.couleur = couleur
        self.trajet = trajet
        self.grille = grille
        
    def autourVoyageur(self,position):
        """determine le contenu des cases autour du voyageur (soit un autre voyageur, soit un obstacle, soit une porte) ;
        en entree : les coordonnees du voyageur (tuple d'entiers) ; en sortie : la listes des cases accessibles (tuples d'entiers) """
        casespossibles=[]
        x_voy=position[0]
        y_voy=position[1]
        for case in [(x_voy-1, y_voy-1), (x_voy-1, y_voy), (x_voy-1, y_voy+1), (x_voy, y_voy-1), (x_voy, y_voy+1), (x_voy+1, y_voy-1),(x_voy+1, y_voy), (x_voy+1, y_voy+1)]:
            contenu = self.grille.getContenuCase(case)
            if contenu[0]==None and contenu[1]==None: # case accessible
                casespossibles.append(case)               
        return casespossibles
            
        
    def seDeplacer(self):
        """ deplacement d'un voyageur. Sortie : nouvelle position du voyageur (tuple d'entiers).
        """
        maposition=self.grille.getPosition(self)
        casespossibles=autourVoyageur(maposition) 
        if casespossibles==[] : return(maposition) # aucune case accessible, le voyageur ne bouge pas
        else :
            maxi = -1
            for coord in casespossibles:
                if coord in self.trajet :
                    self.trajet.pop(coord)
                    if self.trajet ==[] : grille.deleteVoyageur(self)
                    return coord
                else :
                    vecteur1=(self.trajet[0][0] - maposition[0], self.trajet[0][1] - maposition[1])
                    vecteur2=(coord[0] - maposition[0], coord[1] - maposition[1])
                    cosinus = (vecteur1[0]*vecteur2[0] + vecteur1[1]*vecteur2[1])/(sqrt(vecteur1[0]**2 + vecteur1[1])*sqrt(vecteur2[0]**2 + vecteur2[1]))
                    if cosinus >= maxi :
                        maxi = cosinus
                        new_pos=coord
                    
        return new_pos
    
    
class Obstacle:
    def __init__(self, couleur, grille):
        self.couleur = couleur
        self.grille = grille

class Porte:
    def __init__(self, couleur, grille):
        self.couleur = couleur
        self.grille = grille
        
