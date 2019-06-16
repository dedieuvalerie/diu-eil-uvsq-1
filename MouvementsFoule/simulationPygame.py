import pygame
import scenario01 as scene
import math

pygame.init()

TAILLE_CELLULE = 15  # nb de pixels par cellule 
DIM_X          = TAILLE_CELLULE * scene.DIM_X
DIM_Y          = TAILLE_CELLULE * scene.DIM_Y
SCREEN         = pygame.display.set_mode((DIM_X, DIM_Y))
CASE           = pygame.Surface((TAILLE_CELLULE, TAILLE_CELLULE))
COULEUR_FOND   = (255, 255, 255)
FRAME_DELAY    = 10 # en ms

def toPixel(pos):
    (x, y) = pos
    return (x * TAILLE_CELLULE, y * TAILLE_CELLULE)

def dessineObstacles():
    obstacles = scene.g.getObstacles()
    for pos in obstacles.keys():
        obst = obstacles[pos]
        CASE.fill(obst.couleur)
        SCREEN.blit(CASE, toPixel(pos))

def dessinePortes():
    portes    = scene.g.getPortes()
    for pos in portes.keys():
        porte = portes[pos]
        CASE.fill(porte.couleur)   
        SCREEN.blit(CASE, toPixel(pos))       

def dessineVoyageurs():
    def dessinVoyageur(pos, v):
        (x, y)= toPixel(pos)
        cpos = (x + TAILLE_CELLULE // 2, y + TAILLE_CELLULE // 2)
        pygame.draw.circle(SCREEN, v.couleur, cpos, 
                           TAILLE_CELLULE // 2, 0)    
    voyageurs  = scene.g.getVoyageurs()
    for pos in voyageurs.keys():
        voy = voyageurs[pos]
        dessinVoyageur(pos, voy)
        
def effaceVoyageurs():
    voyageurs = scene.g.getVoyageurs()
    for pos in voyageurs.keys():
        CASE.fill(COULEUR_FOND)
        SCREEN.blit(CASE, toPixel(pos)) 

def main():
    SCREEN.fill(COULEUR_FOND)
    dessineObstacles()
    dessinePortes()
    dessineVoyageurs()
    step = 0
    scene.injecteVoyageurs()
    while not pygame.event.poll().type == pygame.QUIT:
        startTicks = pygame.time.get_ticks()
        step += 1
        nbVoy = scene.g.nbVoyageursSortis
        debitMoy = float(nbVoy) / step
        nbPasMoy = math.inf if nbVoy == 0 else (
            float(scene.g.sommePas) / nbVoy)
        tempsMoy = math.inf if nbVoy == 0 else (
            float(scene.g.sommeTemps) / nbVoy)
        mTemplate = ("trame {:d}, {:d} voyageurs écoulés, " +
                     "environ {:f} voyageurs/trame, couloir franchi avec " +
                     "une moyenne de {:f} pas et de {:f} trames")
        message = mTemplate.format(step, nbVoy, debitMoy, nbPasMoy, tempsMoy)
        print(message)
        effaceVoyageurs()
        scene.injecteVoyageurs()
        scene.g.deplacements()
        dessinePortes()
        dessineVoyageurs()
        pygame.display.flip()
        endTicks = pygame.time.get_ticks()
        pygame.time.wait(max(0, FRAME_DELAY - endTicks + startTicks))
    pygame.quit()
    
main()
