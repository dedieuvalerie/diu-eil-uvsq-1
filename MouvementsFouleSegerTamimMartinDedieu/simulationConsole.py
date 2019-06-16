import scenario01 as scene
import math

##################
### simulation ###
##################

def nbVoyageur():
    return len(scene.g.getVoyageurs().values())

step = 0
scene.injecteVoyageurs()
print(scene.g)
while nbVoyageur() > 0:
    print("\033[2J\033[;H") # ou os.system("cls")
    scene.g.deplacements()
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
    print(scene.g)
    scene.injecteVoyageurs()