
import environnement
import grille

dim=800
taille=20
boucle=int(dim/taille)-1

def decor(g):
    noir = (0, 0, 0)
    rouge = (255, 0, 0)
    vert = (0, 255, 0)
    vertclair=(200,255,200)
    
    
    # création des obstacles (mur, zone d'évitement, ...)
    
    Liste_obstacle=[]
    
    #côté gauche
    
    for k in range(boucle):
        Liste_obstacle.append((0,k))
        
    #en haut
    for k in range(1,boucle+1):
       Liste_obstacle.append( (k,0) )
    
            
    # a droite
    
    for k in range (1,boucle-4):
        
            Liste_obstacle.append((boucle,k))
            
    #en bas
    
    for k in range(0,boucle+1):
        Liste_obstacle.append( (k,boucle))
    
    
    #au milieu    (mur du milieu)
    for k in range(4,boucle):
        Liste_obstacle.append( (int(boucle/2),k))  
    
    
    
    #un obstacle après le mur du milieu    
        
    for i in range(int(boucle/2)+2,int(boucle/2)+9):
         for j in range(4,7):        
             Liste_obstacle.append((i,j))   
    #et un autre         
    for j in range(int(boucle/2),int(boucle/2)+5):
                 
             Liste_obstacle.append((boucle-6,j))  
             
    #et un autre         
    for j in range(int(boucle/2),int(boucle/2)+3):
                 
             Liste_obstacle.append((boucle-9,j))           
        
    obs1 = environnement.Obstacle(noir, g)
    g.addObstacle(Liste_obstacle, obs1)
    
    
    
    
    
        
    # création de la porte de sortie
    p1 = environnement.Porte(vertclair, g)
    
    
    
    #les passages
    p2 = environnement.Porte(vert, g)
    
    
    
    
    
    #a droite(la sortie)
    Liste_Porte1=[(boucle,k) for k in range(boucle-4,boucle)]
    
   
    
    
    #les passages
    
    
    Liste_Porte2=[(int(boucle/2),k) for k in range(1,4)]
    
    
    
    g.addPorte(Liste_Porte1, p1)
    g.addPorte(Liste_Porte2, p2)
    
    
    # création des voyageurs
    Coord_Voyageurs=[(3,3),(4,3),(5,3),  (3,4),(4,4),(5,4), 
    
    (2,boucle-5),(3,boucle-5),(4,boucle-5),
    (2,boucle-4),(3,boucle-4),(4,boucle-4),
    (2,boucle-3),(3,boucle-3),(4,boucle-3),
    
    (int(boucle/4),int(boucle/4)),(int(boucle/4)+1,int(boucle/4)),
    (int(boucle/4),int(boucle/4)+1),(int(boucle/4)+1,int(boucle/4)+1),
    (int(boucle/4),int(boucle/4)+2),(int(boucle/4)+1,int(boucle/4)+2),
    
    (int(boucle/2)-5,boucle-4),(int(boucle/2)-4,boucle-4),(int(boucle/2)-3,boucle-4),
    (int(boucle/2)-5,boucle-3),(int(boucle/2)-4,boucle-3),(int(boucle/2)-3,boucle-3),
    (int(boucle/2)-5,boucle-2),(int(boucle/2)-4,boucle-2),(int(boucle/2)-3,boucle-2),
    
    
    #de l'autre côté du mur du milieu
    (int(boucle/2)+5,boucle-4),(int(boucle/2)+6,boucle-4),(int(boucle/2)+7,boucle-4),
    (int(boucle/2)+5,boucle-3),(int(boucle/2)+6,boucle-3),(int(boucle/2)+7,boucle-3),
    (int(boucle/2)+5,boucle-2),(int(boucle/2)+6,boucle-2),(int(boucle/2)+7,boucle-2),
    
     ]
    
    
    
    
   
    
    
    for k in range(len(Coord_Voyageurs)):
        
        #trajet du voyageur avant le mur du milieu
        if Coord_Voyageurs[k][0]<int(boucle/2):
           g.addVoyageur( Coord_Voyageurs[k] ,environnement.Voyageur(rouge, [p2,p1], g) )
        #trajet du voyageur après le mur du milieu
        else:
           g.addVoyageur( Coord_Voyageurs[k] ,environnement.Voyageur(rouge, [p1], g) )












