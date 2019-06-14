import functools as ft
import random
import environnement
from astropy.table import row

class Grille:
    """
    Represente le 'terrain' ou evoluent les elements de la simulation.
    Une grille est creee vierge puis on lui ajoute differents elements qui 
    occupent sur une ou plusieurs coordonnees.
    Les liens entre objets et coordonnees est maintenu par des dictionnaires 
    Une coordonnee non occupee est juste asbente des clefs.
    Les objets mobiles (voyageurs) dialoguent avec la grille au travers de 
    differentes methodes
    """
    def  __init__(self):
        """ 
        voyageurs, obstacles et portent sont conserves dans trois attributs 
        differents, de type dictionnaire avec des coordonnees (couple de int)
        comme clefs
        """
        self.voyageurs = dict()
        self.obstacles = dict()
        self.portes = dict()
        
    def addVoyageur(self, coord, v):
        """
        Ajoute un voyageur,sur UNE certaine coordonnee, dans le dictionnaire
        des voyageurs.
        """
        assert(coord not in self.voyageurs.keys())
        self.voyageurs[coord] = v
    
    def addObstacle(self, coords, m):
        """
        Ajoute un obstacle,sur certaineS coordonneeS, dans le dictionnaire
        des obstacles.
        """
        for coord in coords:
            assert coord not in self.obstacles.keys(), str(coord) + " occupee"
            self.obstacles[coord] = m
    
    def addPorte(self, coords, p):
        """
        Ajoute une porte,sur certaineS coordonneeS, dans le dictionnaire
        des portes.
        """
        for coord in coords:
            assert(coord not in self.portes.keys())
            self.portes[coord] = p
    
    def getVoyageurs(self):
        """
        Retourne le dictionnaire des voyageurs.
        Il sera aproprie, ulterieurement de faire une copie
        """
        # pas de copie (pour l'instant)
        return self.voyageurs
    
    def getObstacles(self):
        """
        Retourne le dictionnaire des obstacles.
        Il sera aproprie, ulterieurement de faire une copie
        """
        # pas de copie (pour l'instant)
        return self.obstacles
    
    def getPortes(self):
        """
        Retourne le dictionnaire des portes.
        Il sera aproprie, ulterieurement de faire une copie
        """
        # pas de copie (pour l'instant)
        return self.portes
    
    def getPosition(self, v):
        """
        Retourne la position d'un voyageur donne du dictionnaire
        des voyageurs
        """
        assert (v in self.voyageurs.values())
        for coord in self.voyageurs.keys():
            if self.voyageurs[coord] == v:
                return coord
    
    def setPosition(self, v, coord):
        """
        Assigne une nouvelle position a un voyageur donne du dictionnaire
        des voyageurs
        """
        positionActuelle = self.getPosition(v)
        assert(coord not in self.voyageurs.keys())
        assert(coord not in self.obstacles.keys())
        self.voyageurs[coord] = self.voyageurs.pop(positionActuelle)
    
    def getContenuCase(self, coord):
        """
        Retourne le (ou les) contenus d'une case donnee.
        A noter que sur une case donnee il peut y avoir un voyageur ET une porte
        """
        mbv = self.voyageurs.get(coord, None)
        mbo = self.obstacles.get(coord, None)
        mbp = self.portes.get(coord, None)
        return (mbv, mbo, mbp)
    
    def getDirection(self, v, p):
        """
        Retourne le vecteur d'origine un voyageur donne et d'extremite
        le point moyen d'une porte donnee
        """
        coords = [coord for coord in self.portes if (self.portes[coord] == p)]
        size = len(coords)
        assert(size != 0)
        (sx, sy) = (0, 0)
        for (x, y) in coords:
            sx += x
            sy += y
        (vx, vy) = self.getPosition(v)
        return ((sx / size) - vx, (sy / size) - vy)
        
    def deleteVoyageur(self, v):
        """
        Commande a la grille "d'oublier" un voyageur donne
        """
        position = self.getPosition(v)
        self.voyageurs.pop(position)
        
    def deplacements(self):
        """
        Active un 'tour' de placement pour chaque voyageur present dans
        la grille
        """
        # ne pas iterer sur un objet que l'on modifie !
        # A FAIRE : melanger auparavant la liste des voyageurs
        voys = [self.voyageurs[coord] for coord in self.voyageurs.keys()]
        for v in voys:
            new_pos=v.seDeplacer()
            grille.deleteVoyageur(v)
            grille.addVoyageur(new_pos,v)
            
            
            
            
    def __str__(self):
        """
        Representation textuelle sommaire de la grille
        """
#         coords = self.obstacles.keys()
        minx = min([coords[0] for coords in 
                    (list(self.voyageurs) + list(self.obstacles) + list(self.portes))])
        maxx = max([coords[0] for coords in 
                    (list(self.voyageurs) + list(self.obstacles) + list(self.portes))])
        miny = min([coords[1] for coords in 
                    (list(self.voyageurs) + list(self.obstacles) + list(self.portes))])
        maxy = max([coords[1] for coords in 
                    (list(self.voyageurs) + list(self.obstacles) + list(self.portes))])
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
