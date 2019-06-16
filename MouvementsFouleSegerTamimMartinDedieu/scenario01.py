import grille
import environnement
import random
# import os

DIM_X = 80
DIM_Y = 20

blanc =  (255, 255, 255)
gris = (150, 150, 150)
noir = (0, 0, 0)
rouge = (255, 0, 0)
vert = (0, 255, 0)
vert_clair = (0, 10, 0)
bleu = (0, 0, 255)

g = grille.Grille()

################
### les murs ###
################

# enceinte
posMurs = [(0, y) for y in range(0, DIM_Y)]
posMurs += [(DIM_X - 1, y) for y in range(0, DIM_Y)]
posMurs += [(x, 0) for x in range(1, DIM_X - 1)]
posMurs += [(x, DIM_Y - 1) for x in range(1, DIM_X - 1)]

# mur percé central
posMurs += [(50, y) for y in range(1, DIM_Y - 1) if y <= 6 or y > 12]
posMurs += [(49, y) for y in range(1, 6)]
posMurs += [(48, y) for y in range(1, 5)]
posMurs += [(47, y) for y in range(1, 4)]
posMurs += [(46, y) for y in range(1, 3)]
posMurs += [(45, y) for y in range(1, 2)]

# pilier avant
posMurs += [(30, y) for y in range(1, DIM_Y - 1) if y > 6 and y <= 12]
posMurs += [(29, y) for y in range(1, DIM_Y - 1) if y > 7 and y <= 11]
posMurs += [(28, y) for y in range(1, DIM_Y - 1) if y > 8 and y <= 10]
posMurs += [(27, y) for y in range(1, DIM_Y - 1) if y > 9 and y <= 9]

# pilier arriere
posMurs += [(70, y) for y in range(1, DIM_Y - 1) if y > 6 and y <= 12]
posMurs += [(69, y) for y in range(1, DIM_Y - 1) if y > 7 and y <= 11]
posMurs += [(68, y) for y in range(1, DIM_Y - 1) if y > 8 and y <= 10]
posMurs += [(67, y) for y in range(1, DIM_Y - 1) if y > 9 and y <= 9]

# piège à voyageur !
posMurs += [(49, 13)]

mur = environnement.Obstacle(gris, g)
g.addObstacle(posMurs, mur)


##################
### les portes ###
##################

# porte correspondant au point de départ
posPorteDep = [(1, y) for y in range(1, DIM_Y - 1)]
posPorteDep += [(x, y) for x in range(20, 26) for y in range(4, DIM_Y - 4) if 
                y <= 6 or y >= DIM_Y - 7]
porteDep = environnement.Porte(blanc, g)
g.addPorte(posPorteDep, porteDep)

# porte intermédiaire 0
posPorte0 = [(32, y) for y in range(2, DIM_Y - 2)]
posPorte0 += [(x, 6) for x in range(33, 49)]
posPorte0 += [(x, 13) for x in range(33, 46)]
porte0 = environnement.Porte(blanc, g)
g.addPorte(posPorte0, porte0)

# porte intermédiaire 1
posPorte1 = [(50, y) for y in range(7, 13)]
porte1 = environnement.Porte(blanc, g)
g.addPorte(posPorte1, porte1)

# porte de sortie 3
posPorte3 = [(78, y) for y in range(1, 5)]
porte3 = environnement.Porte(vert, g)
g.addPorte(posPorte3, porte3)

# porte de sortie 4
posPorte4 = [(78, y) for y in range(DIM_Y - 5, DIM_Y - 1)]
porte4 = environnement.Porte(vert, g)
g.addPorte(posPorte4, porte4)


#####################
### les voyageurs ###
#####################

trajet1 = [porteDep, porte0, porte1, porte3]
trajet2 = [porteDep, porte0, porte1, porte4]
posInjection = [(1, y) for y in range(1, DIM_Y - 1)]

def addNewVoyageur(pos):
    couleur = (0, 0, 0)
    if random.random() < 0.5:
        couleur = (random.randint(100, 255), random.randint(0, 255), 10)
        trajet = trajet1
    else:
        couleur = (10, random.randint(0, 255), random.randint(100, 255))
        trajet = trajet2
    v = environnement.Voyageur(couleur, trajet, g)
    g.addVoyageur(pos, v)
    
def injecteVoyageurs():
    MAX_INJECTION = 3 # si 4 : EMBOUTEILLAGE MONSTREUX ASSURE !
    injection = [pos for pos in posInjection if 
                 g.getContenuCase(pos)[0] == None]
    random.shuffle(injection)
    indice = min(MAX_INJECTION - 1, len(injection))
    for pos in injection[0:indice]:
        addNewVoyageur(pos)
    
