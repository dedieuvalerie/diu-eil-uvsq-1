import environnement
import grille

"""
Petit programme de test de la classe Grille
"""

if __name__ == '__main__':
    noir = (0, 0, 0)
    rouge = (255, 0, 0)
    vert = (0, 255, 0)
    g = grille.Grille()
    p0 = environnement.Porte(vert, g)
    p1 = environnement.Porte(vert, g)
    p2 = environnement.Porte(vert, g)
    p3 = environnement.Porte(vert, g)
    v1 = environnement.Voyageur(rouge, [p0, p1], g)
    v2 = environnement.Voyageur(rouge, [p0, p1], g)
    v3 = environnement.Voyageur(rouge, [p2, p0, p3], g)
    obs1 = environnement.Obstacle(noir, g)
    g.addObstacle([(0, 0), (5, 4), (5, 5), (6, 5), (9, 9), (8, 5), (9, 5), (10, 5), (11, 5)], obs1)
    g.addVoyageur((1, 1), v1)
    g.addVoyageur((2, 1), v2)
    g.addVoyageur((0, 9), v3)
    g.addPorte([(9, 3), (9, 4)], p0)
    g.addPorte([(7, 8), (7, 9)], p1)
    g.addPorte([(7, 5)], p2)
    g.addPorte([(11, 0)], p3)
    step = 0
    print(step)
    print(g)
    while (v1 in g.getVoyageurs().values() or v2 in g.getVoyageurs().values() or 
           v3 in g.getVoyageurs().values()):
        step += 1
        g.deplacements()
        print(step)
        print(g)
    print("fini !")