from grille import Grille
from math import *

class Voyageur:
    """
    Représente les éléments mobiles qui se déplacent dans la grille donnée à la
    construction.
    L'attribut couleur peut servir à l'affichage.
    L'attribut trajet consiste en un liste de portes. 
    Lorsque cette liste est vide, le voyageur est arrivé et peut disparaître de
    la grille.
    La dernière porte est donc la porte d'arrivée.
    Les portes intermédiaires jouent un peu le rôle des panneau indicateurs 
    placés dans la salle et qui indiquent au voyageur des buts intermédiaires.
    Ces portes intermédiaires semblent indispensables si on ne souhaite pas 
    (comme c'est indiqué dans les consignes) que le voyageur ne connaisse pas 
    tout son environnement et si, comme cela est souhaitable dans la réalité, 
    que le voyageur ne se lance pas dans une exploration plus ou moins aléatoire 
    d'un labyrinthe. Les portes du trajet doivent être placées de telle façon 
    qu'à chaque moment de son déplacement, le voyageur ait 'en visuel' son 
    prochain but.
    A FAIRE : afin de rendre un peu aléatoire (de façon simple) le déplacement
    de la foule on peut imaginer rajouter comme attribut une probabilité de 
    déplacement (tirée au hasard lors de la construction ou spécifiée lors 
    de celle-ci). Ainsi, lorsque la grille ordonne au voyageur de se déplacer,
    le voyageur ne se déplace pas systématiquement.
    """
    def __init__(self, couleur, trajet, grille):
        self.couleur = couleur
        self.trajet = trajet
        self.grille = grille
        
    def __autourVoyageur(self,position):
        """
        determine le contenu des cases autour du voyageur (soit un autre 
        voyageur, soit un obstacle, soit une porte) ;
        en entree : les coordonnees du voyageur (tuple d'entiers) ; en sortie : 
        la liste des coordonnees des cases accessibles (tuples d'entiers)
        et avec leur contenu (porte ou vide) 
        """
        casespossibles = []
        x_voy = position[0]
        y_voy = position[1]
        for coord in [(x_voy-1, y_voy-1), (x_voy-1, y_voy), (x_voy-1, y_voy+1), 
                      (x_voy, y_voy-1), (x_voy, y_voy+1), (x_voy+1, y_voy-1),
                      (x_voy+1, y_voy), (x_voy+1, y_voy+1)]:
            contenu = self.grille.getContenuCase(coord)
            if contenu[0] == None and contenu[1] == None: # case accessible
                casespossibles.append((coord, contenu[2]))               
        return casespossibles


    def seDeplacer(self):
        """ 
        deplacement d'un voyageur. 
        Le voyageur commence par observer les cases alentour et etablit ainsi 
        une liste de possibilites.
        Si une des cases accessibles est une des etapes de son trajet, il y va. 
        Sinon, on choisit celle qui le devie le moins possible de son trajet
        (produit scalaire de deux vecteurs) 
        """
        maposition = self.grille.getPosition(self)
        casespossibles = self.__autourVoyageur(maposition)
        if self.trajet == []:
            self.grille.deleteVoyageur(self)
        elif self.trajet[0] == self.grille.getContenuCase(maposition)[2]:
            self.trajet.pop(0)
            self.seDeplacer()
        elif casespossibles != []: 
            maxi = -1
            dir = self.grille.getDirection(self, self.trajet[0])
            normDir = sqrt(dir[0] * dir[0] + dir[1] * dir[1])
            for case in casespossibles:
                posCase = case[0]
                vDep = (posCase[0] - maposition[0], posCase[1] - maposition[1])
                normVDep = sqrt(vDep[0] * vDep[0] + vDep[1] * vDep[1])
                pDot = dir[0]*vDep[0] + dir[1]*vDep[1]
                cosinus = pDot / (normDir * normVDep)
                if cosinus >= maxi :
                    maxi = cosinus
                    new_pos = posCase
            if maxi > 0:
                self.grille.setPosition(self, new_pos)
    
class Obstacle:
    def __init__(self, couleur, grille):
        self.couleur = couleur
        self.grille = grille

class Porte:
    def __init__(self, couleur, grille):
        self.couleur = couleur
        self.grille = grille
        