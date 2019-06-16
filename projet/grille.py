import functools as ft
from random import *
import environnement

class Grille:
    """
    Représente le 'terrain' où évoluent les éléments de la simulation.
    Une grille est créée vierge puis on lui ajoute différents éléments qui 
    occupent une ou plusieurs coordonnées (ou 'case's).
    Les liens entre objets et coordonnées est maintenu par des dictionnaires 
    Une case non occupée est juste asbente des clefs des dictionnaires.
    Les objets mobiles (voyageurs) dialoguent avec la grille pour juger de 
    leur environnement au travers de différentes méthodes ; ils peuvent aussi
    demander à la grille de les enregistrer à une nouvelle position.
    """
    def  __init__(self):
        """ 
        voyageurs, obstacles et portes sont conservés dans trois attributs 
        différents, de type dictionnaire avec des coordonnées (couple de int)
        comme clefs
        """
        self.voyageurs = dict()
        self.obstacles = dict()
        self.portes = dict()
        
    def addVoyageur(self, coord, v):
        """
        Ajoute un voyageur,sur _UNE_ certaine coordonnée, dans le dictionnaire
        des voyageurs.
        """
        assert(coord not in self.voyageurs.keys())
        self.voyageurs[coord] = v
    
    def addObstacle(self, coords, m):
        """
        Ajoute un obstacle,sur _certaineS_coordonnéeS_, dans le dictionnaire
        des obstacles.
        """
        for coord in coords:
            assert coord not in self.obstacles.keys(), str(coord) + " occupée"
            self.obstacles[coord] = m
    
    def addPorte(self, coords, p):
        """
        Ajoute une porte,sur _certaineS_coordonnéeS_, dans le dictionnaire
        des portes.
        """
        for coord in coords:
            assert(coord not in self.portes.keys())
            self.portes[coord] = p
    
    def getVoyageurs(self):
        """
        Retourne le dictionnaire des voyageurs.
        Il sera aproprié, ultérieurement de faire une copie
        """
        # pas de copie (pour l'instant)
        return self.voyageurs
    
    def getObstacles(self):
        """
        Retourne le dictionnaire des obstacles.
        Il sera aproprié, ultérieurement de faire une copie
        """
        # pas de copie (pour l'instant)
        return self.obstacles
    
    def getPortes(self):
        """
        Retourne le dictionnaire des portes.
        Il sera aproprié, ultérieurement de faire une copie
        """
        # pas de copie (pour l'instant)
        return self.portes
    
    def getPosition(self, v):
        """
        Retourne la position d'un voyageur donné du dictionnaire
        des voyageurs.
        En cas de très nombreux voyageurs, pourrait poser des problèmes de 
        performance : le cas échéant on pourra maintenir un dictionnaire inversé
        voyageur -> coordonnées (à initialiser dans le constructeur et
        à tenir à jour dans les méthodes addVoyageur et setPosition)
        """
        assert (v in self.voyageurs.values())
        for coord in self.voyageurs.keys():
            if self.voyageurs[coord] == v:
                return coord
    
    def setPosition(self, v, coord):
        """
        Assigne une nouvelle position à un voyageur donné du dictionnaire
        des voyageurs
        """
        positionActuelle = self.getPosition(v)
        assert(coord not in self.voyageurs.keys())
        assert(coord not in self.obstacles.keys())
        self.voyageurs[coord] = self.voyageurs.pop(positionActuelle)
    
    def getContenuCase(self, coord):
        """
        Retourne le (ou les) contenus d'une case donnée.
        sous la forme d'un triple. Le premier élément est soit le voyageur
        présent sur la case soit None, idem pour le second élément mais pour un
        éventuel obstacle, idem pour le troisème élément mais pour une 
        éventuelle porte.
        A noter que sur une case donnée il peut y avoir un voyageur ET une porte
        """
        mbv = self.voyageurs.get(coord, None)
        mbo = self.obstacles.get(coord, None)
        mbp = self.portes.get(coord, None)
        return (mbv, mbo, mbp)
    
    def getDirection(self, v, p):
        """
        Retourne le vecteur d'origine un voyageur donné et d'extrémité
        le point moyen d'une porte donnée le plus proche de l'origine
        (on pourrait imaginer par exemple prendre pour extrémité le 
        'point moyen' de la porte mais cela ne semble a priori pas judicieux).
        Là encore, s'il y a de très nombreuses portes (peu probable) et si des 
        problèmes de performance apparaîssent, ne pas hésiter utiliser un
        dictionnaire porte -> [coord] maintenu par le constructeur et la
        méthode addPorte.
        """
        (vx, vy) = self.getPosition(v)
        coords = [coord for coord in self.portes if (self.portes[coord] == p)]
        size = len(coords)
        assert(size != 0)
        # version 'point moyen'
#         # fold ou reduce en python ???
#         (sx, sy) = (0, 0)
#         for (x, y) in coords:
#             sx += x
#             sy += y
#         return ((sx / size) - vx, (sy / size) - vy)
        # version point le plus proche
        # zipWith en python ???
        zipped =  [(c, (vx - c[0]) * (vx - c[0]) + (vy - c[1]) * (vy - c[1])) 
                   for c in coords]
        # minBy en python ???
        mind2 = min([c_d2[1] for c_d2 in zipped])
        (ex, ey) = [x[0] for x in zipped if x[1] == mind2][0]
        return (ex - vx, ey - vy)
        
    def deleteVoyageur(self, v):
        """
        Commande à la grille "d'oublier" un voyageur donné, c'est à dire de le 
        faire disparaître du dictionnaire correspondant.
        """
        position = self.getPosition(v)
        self.voyageurs.pop(position)
        
    def deplacements(self):
        """
        Active un 'tour' de placement pour chaque voyageur présent dans
        la grille.
        ATTENTION à ne pas iterer sur un objet que l'on modifie !
        """
        voys = [self.voyageurs[coord] for coord in self.voyageurs.keys()]
        shuffle(voys) # pour introduire un peu d'aléatoire
        for v in voys:
            v.seDeplacer()
            
    def __str__(self) -> str:
        """
        Représentation textuelle sommaire de la grille, utile à des fins de
        mise au point.
        """
        # calcul de la 'bonding box' de la grille
        minx = min([coords[0] for coords in 
                    (list(self.voyageurs) + list(self.obstacles) + 
                     list(self.portes))])
        maxx = max([coords[0] for coords in 
                    (list(self.voyageurs) + list(self.obstacles) + 
                     list(self.portes))])
        miny = min([coords[1] for coords in 
                    (list(self.voyageurs) + list(self.obstacles) + 
                     list(self.portes))])
        maxy = max([coords[1] for coords in 
                    (list(self.voyageurs) + list(self.obstacles) + 
                     list(self.portes))])
        # création de la chaîne
        txt = ""
        for y in range(miny, maxy + 1):
            row = ""
            for x in range(minx, maxx + 1):
                v = self.voyageurs.get((x, y), None)
                m = self.obstacles.get((x, y), None)
                p = self.portes.get((x, y), None)
                if v != None:
                    row += 'v'
                elif m != None:
                    row += 'o'
                elif p != None:
                    row += 'p'  
                else:
                    row += "."  
            row += "\n"
            txt += row
        return txt