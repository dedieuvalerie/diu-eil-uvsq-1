import pygame
import environnement
import grille
import scenario2





dim=800  #dimension de la fenetre
taille=20  #taille d'une cellule 
boucle=int(dim/taille)


        
        
        
        
def afficher_voyageur(screen,x,y,couleur):
    
    pygame.draw.circle(screen,couleur,(x*taille+int(taille/2),y*taille+int(taille/2)),int(taille/2),0)    
        
def dessiner_grille(screen):
    for i in range(boucle):
        for j in range(boucle):
            
            
    
            pygame.draw.line(screen,(0,0,0),(i*taille,0),(i*taille,dim),1)
            pygame.draw.line(screen,(0,0,0),(0,j*taille),(dim,j*taille),1)
            
            
def afficher_obstacle_porte(screen,x,y,couleur):
    
    case=pygame.Surface((taille,taille))
    case.fill(couleur)
    screen.blit(case,(x*taille,y*taille))
    
def fond(screen,g):
    
    
    #on récupère les coordonnées des obstacles,portes,des voyageurs(mobiles)
    
    #g = grille.Grille()
    
    #on récupère les coordonnées des obstacles
    OBSTACLES=g.getObstacles()
    
    #on récupère les coordonnées des portes
    PORTES=g.getPortes()
    
    
    dessiner_grille(screen)
    
    
    #case = pygame.Surface((taille,taille)) # une surface grise
 
            
    red=(255,0,0)
    blue=(0,0,255)        
    #on place les obstacles
    #test
    #OBSTACLES={(3,3):red,(10,10):red}
    for obstacle in OBSTACLES.keys():
        # on réupère l'objet obstacle
        obst=OBSTACLES[obstacle]
        
        #ligne test
        #afficher_obstacle_porte(screen,obstacle[0],obstacle[1],obst)
        
        #ligne suivante du projet
        afficher_obstacle_porte(screen,obstacle[0],obstacle[1],obst.couleur)
        
        
        # case.fill(obst.couleur)
        # screen.blit(case,obstacle)
    #on place les portes
    #PORTES={(0,0):blue,(1,0):blue , (2,0):blue,(3,0):blue ,(4,0):blue,(10,0):blue,(10,1):blue,(10,2):blue,(10,3):blue}
    
    
    for porte in PORTES.keys():
        
        p=PORTES[porte]
        
        #ligne test
        #afficher_obstacle_porte(screen,porte[0],porte[1],p)
        
        #ligne du projet
        afficher_obstacle_porte(screen,porte[0],porte[1],p.couleur)
        
        # case.fill(p.couleur)   
        # screen.blit(case,porte) 
    
        
        
            
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
        afficher_voyageur(screen,voyageur[0],voyageur[1],v.couleur)
        
    
    
    
               
    
    pygame.display.flip()
    
    
   
    
    
      

def main():
    
    pygame.init()
    size=[dim,dim]
    
    screen=pygame.display.set_mode(size)
    
    g=grille.Grille()
    scenario2.decor(g)
   
    
    while 1:
        event = pygame.event.poll()  
        if event.type == pygame.QUIT: break 
        
        pygame.time.delay(150)
        #g=grille.Grille()
        g.deplacements()
        
        affichage(screen,g)
       
        
    pygame.quit()
    
main()