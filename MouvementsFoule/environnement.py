#import grille
from math import *
import random

class Voyageur:
    """
    Représente les éléments mobiles qui se déplacent dans la grille donnée à la
    construction.
    L'attribut couleur peut servir à l'affichage.
    L'attribut trajet consiste en un liste de portes par lesquelles doit passer
    le voyageur. Lorsque cette liste a été intégralement parcourue, 
    le voyageur est arrivé et peut disparaître de la grille.
    Afin de simuler des vitesses (statistiquement) différentes pour les 
    voyageurs, un attribut probaDep contient une probabilité de 
    déplacement (tirée au hasard lors de la construction ou spécifiée lors 
    de celle-ci). Ainsi, lorsque la grille ordonne au voyageur de se déplacer,
    le voyageur ne se déplace pas systématiquement.
    Le voyageur possède aussi un compteur de pas qui compte tous les pas 
    effectués.
    Le compteur temps comptabilise lui toutes les trames où on l'a solicité pour
    tenter un mouvement.
    lors de la simulation, un autre compteur de pas de type 'watch dog' 
    permet d'enclencher, comme le ferait un vrai voyageur, une procédure de 
    'perte' qui tente de la ramener à la dernière porte qui a 
    été vue. Il convient ainsi, bien que ce ne soit pas imposé dans la classe
    de positionner une porte à l'endroit exact où le voyageur est déposé dans 
    la grille (pour qu'il connaisse son point de départ).
    
    Dans le déplacement d'un voyageur, les portes intermédiaires jouent un peu 
    le rôle des panneau indicateurs  placés dans la salle et qui indiquent au 
    voyageur des buts intermédiaires. Ce serait plus exactement l'équivalent 
    du marquage au plafond de zones qui guident le voyageur d'étapes en étapes 
    jusqu'à l'objectif final.
    Ces portes intermédiaires semblent indispensables si on ne souhaite pas 
    (comme c'est indiqué dans les consignes) que le voyageur  connaisse  
    tout son environnement et si, comme cela est souhaitable dans la réalité, 
    que le voyageur se lance dans une exploration plus ou moins aléatoire 
    d'un labyrinthe. Les portes du trajet doivent être placées de telle façon 
    qu'à chaque moment de son déplacement, le voyageur ait 'en visuel' son 
    prochain but. En fait, le placement des panneaux indicateurs fait partie 
    intégrante de la conception d'une salle et le programme doit permettre de 
    tester cela.
    """
    def __init__(self, couleur, trajet, grille, probaDep = None):
        self.couleur = couleur
        self.trajet = trajet
        self.indiceTrajet = 0
        self.grille = grille
        if probaDep == None:
            ### ATTENTION ###
            # la valeur de sigma joue enormement sur la fluidité
            self.probaDep = random.gauss(0.8, 0.1)
        else:
            self.probaDep = probaDep
        self.podometre = 0
        self.temps = 0
        self.WATCH_DOG_VAL = 100
        self.watchDog = self.WATCH_DOG_VAL
        self.perdu = False
        
    def _scruteHorizon(self,position):
        """
        determine le contenu des cases autour du voyageur (soit un autre 
        voyageur, soit un obstacle, soit une porte) ;
        en entree : les coordonnees du voyageur (tuple d'entiers) ; en sortie : 
        la liste des coordonnees des cases accessibles (tuples d'entiers)
        et avec leur contenu (porte ou vide) 
        """
        (x_voy, y_voy) = position
        horizonRel = [(x, y) for x in [-1, 0, 1] for y in [-1, 0, 1] 
                   if x != 0 or y != 0]
        posHorizon = [(x_voy + dep[0], y_voy + dep[1]) for dep in horizonRel]
        contHorizon = [(pos, self.grille.getContenuCase(pos)) for 
                       pos in posHorizon]
        def estLibre(cont):
            return cont[1][0] == None and cont[1][1] == None
        cases = [cont for cont in contHorizon if estLibre(cont)]
        random.shuffle(cases)
        return cases


    def seDeplacer(self):
        """ 
        Deplacement d'un voyageur. 
        Le voyageur commence par observer les cases alentour et etablit ainsi 
        une liste de possibilites.
        Si une des cases accessibles est une des etapes de son trajet, il y va. 
        Sinon, on choisit celle qui le devie le moins possible de son trajet
        (produit scalaire de deux vecteurs) 
        """
        def initWatchDog():
            self.watchDog = (self.WATCH_DOG_VAL if not self.perdu else 
                             self.WATCH_DOG_VAL // 5)
        self.temps += 1            
        maposition = self.grille.getPosition(self)
        casesPossibles = self._scruteHorizon(maposition)
        assert(self.indiceTrajet >= 0)
        if len(self.trajet) <= self.indiceTrajet: # arrivé
            self.grille.deleteVoyageur(self)
        elif (self.trajet[self.indiceTrajet] == 
              self.grille.getContenuCase(maposition)[2]): #porte
            self.perdu = False
            initWatchDog()
            self.indiceTrajet += 1
            self.seDeplacer()
        elif self.watchDog == 0:
            self.perdu = not self.perdu
            self.indiceTrajet += -1 if self.perdu else +1 
            initWatchDog()
            self.seDeplacer()
        elif casesPossibles != [] and random.random() < self.probaDep: 
            self.watchDog -= 1
            maxi = -1
            dirP = self.grille.getDirection(
                self, self.trajet[self.indiceTrajet])
            normDir = sqrt(dirP[0] * dirP[0] + dirP[1] * dirP[1])
            for CASE in casesPossibles:
                posCase = CASE[0]
                vDep = (posCase[0] - maposition[0], posCase[1] - maposition[1])
                normVDep = sqrt(vDep[0] * vDep[0] + vDep[1] * vDep[1])
                dotP = dirP[0]*vDep[0] + dirP[1]*vDep[1]
                cosinus = dotP / (normDir * normVDep)
                if cosinus >= maxi :
                    maxi = cosinus
                    new_pos = posCase
            if maxi > 0:
                self.grille.setPosition(self, new_pos)
                self.podometre += 1
        else:
            self.watchDog -= 1

class Obstacle:
    def __init__(self, couleur, grille):
        self.couleur = couleur
        self.grille = grille

class Porte:
    def __init__(self, couleur, grille):
        self.couleur = couleur
        self.grille = grille
        
