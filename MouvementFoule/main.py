import Environnement
import grille

"""
Petit programme de test de la classe Grille
"""

if __name__ == '__main__':
    noir = (0, 0, 0)
    rouge = (255, 0, 0)
    vert = (0, 255, 0)
    g = grille.Grille()
    p1 = environnement.Porte(vert, g)
    voy1 = environnement.Voyageur(rouge, [p1], g)
    obs1 = environnement.Obstacle(noir, g)
    g.addObstacle([(0, 0), (5, 4), (5, 5), (6, 5), (9, 9)], obs1)
    g.addVoyageur((1, 1), voy1)
    g.addPorte([(7, 8), (7, 9)], p1)
    print(g)
    print(g.getContenuCase((0, 0)), g.getContenuCase((1, 1)))
    print(g.getDirection(voy1, p1))
    g.deplacements()
    print(g)
    g.deplacements()
    print(g)
    g.deleteVoyageur(voy1)
    print(g)
    print("fini !")
