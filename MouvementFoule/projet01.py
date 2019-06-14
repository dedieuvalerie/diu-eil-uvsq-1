import pygame
import environnement
import grille



couleur_Obstacle=((255,0,0))

dim=800  #dimension de la fenetre
taille=20  #taille d'une cellule 
boucle=int(dim/taille)


        
        
        
        
def dessiner_cercle(screen,x,y,couleur):
    pygame.draw.circle(screen,couleur,(x,y),10,0)    
        
def dessiner_grille(screen):
    for i in range(boucle):
        for j in range(boucle):
            
            
    
            pygame.draw.line(screen,(0,0,0),(i*taille,0),(i*taille,dim),1)
            pygame.draw.line(screen,(0,0,0),(0,j*taille),(dim,j*taille),1)

def fond(screen,g):
    
    
    #on récupère les coordonnées des obstacles,portes,des voyageurs(mobiles)
    #Grille.getVoyageurs.keys (on récupère les tuples)
    #Grille.getObstacles.keys  (on récupère les bstacles)
    g = grille.Grille()
    
    #on récupère les coordonnées des obstacles
    OBSTACLES=g.getObstacles()
    
    #on récupère les coordonnées des portes
    PORTES=g.getPortes()
    
    
    dessiner_grille(screen)
    
    
    case = pygame.Surface((taille,taille)) # une surface grise
 
            
            
    #on place les obstacles
    
    for obstacle in OBSTACLES:
        
        obst=OBSTACLES[obstacle]
        case.fill(obst.couleur)
        screen.blit(case,obstacle)
    #on place les portes
    
    for porte in PORTES:
        
        p=PORTES[porte]
        case.fill(p.couleur)   
        screen.blit(case,porte) 
    
        
        
            
    pygame.display.flip()

#Là où tout se dessine
def affichage(screen,g):
    #dessin de l'environnement
    screen.fill((255,255,255))
    fond(screen,g)
    
    
    #On récupère les coordonnées des voyageurs
    #A utiliser plutôt avec une copie
    
    VOYAGEURS=g.getVoyageurs()
    
    
    
    #on place les voyageurs    
    for voyageur in VOYAGEURS:
        
        v=VOYAGEURS[voyageur]
        dessiner_cercle(screen,voyageur[0],voyageur[1],v.couleur)
        # à compléter
    
    
    
               
    
    pygame.display.flip()
    
    
   
    
    
      

def main():
    
    pygame.init()
    size=[dim,dim]
    
    screen=pygame.display.set_mode(size)
    g=grille.Grille()
    
    while 1:
        event = pygame.event.poll()  
        if event.type == pygame.QUIT: break 
        
        g.deplacements()
        affichage(screen,g)
        
    pygame.quit()
    
main()