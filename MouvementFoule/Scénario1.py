class Grille:   
    """ classe Grille """
    def __init__(self, nom, nb_lignes, nb_colonnes):
        self.nb_lignes = nb_lignes
        self.nb_colonnes = nb_colonnes
        self.voyageurs = {}
        self.obstacles = {}
        self.portes = {}
    
    def ajouter_case_obstacle(self, obstacle, position):
        self.obstacles[position] = obstacle
    
    def ajouter_case_porte(self, porte, position):
        self.portes[position] = porte
            
    def ajouter_case_voyageur(self, voyageur, position):
        self.voyageurs[position] = voyageur 

class Obstacle:
    """ Classe Obstacle """
    def __init__(self, position1, position2, grille):
        self.grille = grille
        
        # référencement de l'obstacle dans la grille
        for ligne in range(min(position1[0],position2[0]),max(position1[0],position2[0]) + 1):
            for colonne in range(min(position1[1],position2[1]),max(position1[1],position2[1]) + 1):
                g.ajouter_case_obstacle(self,(ligne,colonne))

class Porte:
    def __init__(self, nom, position1, position2, passage, grille):
        self.nom = nom
        self.passage = passage
        self.grille = grille
        
        # référencement de la porte dans la grille
        for ligne in range(min(position1[0],position2[0]),max(position1[0],position2[0]) + 1):
            for colonne in range(min(position1[1],position2[1]),max(position1[1],position2[1]) + 1):
                g.ajouter_case_porte(self,(ligne,colonne))
                
    def getPortePassage(self):
        return self.passage

class Voyageur:
    def __init__(self, couleur, trajet, position, grille):
        self.couleur = couleur
        self.trajet = trajet
        self.grille = grille
        
        # ajout du voyageur dans la case de la grille 
        grille.ajouter_case_voyageur(self, position)

# création de la grille
g = Grille("Première grille", 15, 20)

# création des obstacles (mur, zone d'évitement, ...)
o = Obstacle((0, 0), (0, 14), g)
o = Obstacle((1, 0), (3, 0), g)
o = Obstacle((6, 0), (12, 0), g)
o = Obstacle((16, 0), (19, 0), g)
o = Obstacle((9, 3), (9, 9), g)
o = Obstacle((13, 4), (15, 6), g)
o = Obstacle((19, 1), (19, 7), g)
o = Obstacle((19, 12), (19, 13), g)
o = Obstacle((3, 14), (19, 14), g)

# création des portes (entrée/sortie, de passage, ...)
pes1 = Porte("Porte E/S 1", (4, 0), (5, 0), False, g)
pes2 = Porte("Porte E/S 2", (13, 0), (15, 0), False, g)
pes3 = Porte("Porte E/S 3", (14, 9), (15, 9), False, g)
pes4 = Porte("Porte E/S 4", (19, 8), (19, 11), False, g)
pes5 = Porte("Porte E/S 5", (1, 14), (2, 14), False, g)
pp1 = Porte("Porte de passage 1", (9, 1), (9, 2), True, g)
pp2 = Porte("Porte de passage 2", (16, 4), (18, 4), True, g)
pp3 = Porte("Porte de passage 3", (10, 6), (12, 6), True, g)
pp4 = Porte("Porte de passage 4", (9, 10), (9, 13), True, g)

# création des voyageurs
v = Voyageur((255, 255, 255), (pes5), (3,2), g)
v = Voyageur((255, 255, 255), (pp4, pes4), (3,3), g)
v = Voyageur((255, 255, 255), (pp1, pp3, pes4), (8,1), g)
v = Voyageur((255, 255, 255), (pp1, pp4, pes4), (6,2), g)
v = Voyageur((255, 255, 255), (pp1, pes5), (13,1), g)
v = Voyageur((255, 255, 255), (pp2, pp4, pes5), (15,1), g)
v = Voyageur((255, 255, 255), (pp3, pes3), (11, 3), g)
v = Voyageur((255, 255, 255), (pes3), (12, 6), g)
v = Voyageur((255, 255, 255), (pp4, pes4), (4, 13), g)
v = Voyageur((255, 255, 255), (pp4, pes4), (5, 13), g)
v = Voyageur((255, 255, 255), (pp4, pes4), (6, 13), g)
v = Voyageur((255, 255, 255), (pp4, pes4), (7, 13), g)
v = Voyageur((255, 255, 255), (pp4, pes4), (8, 13), g)
v = Voyageur((255, 255, 255), (pp2, pp1, pes1), (19, 8), g)
v = Voyageur((255, 255, 255), (pp3, pp1, pes1), (19, 9), g)
v = Voyageur((255, 255, 255), (pp4, pes1), (19, 10), g)
v = Voyageur((255, 255, 255), (pp4, pes5), (19, 11), g)













