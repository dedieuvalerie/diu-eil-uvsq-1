#from typing import List, Set, Dict, Tuple, Optional



import grille



class Voyageur :

    """ cree et determine un voyageur ; attributs : une couleur (tuple de 3 entiers) et une liste trajet contenant les

    differentes etapes pour arriver a la porte finale (tuple de portes) ; cette liste est mise a jour au fur et a mesure

    que les etapes sont franchies ; lorsqu'elle est vide, le voyageur a atteint son but. Ce voyageur appartient a une grille

    (dictionnaire) """

    

    def __init__(self, couleur,trajet, grille):

        self.couleur = couleur

        self.trajet = trajet

        self.grille = grille

        

    def autourVoyageur(self,position):

        """determine le contenu des cases autour du voyageur (soit un autre voyageur, soit un obstacle, soit une porte) ;

        en entree : les coordonnees du voyageur (tuple d'entiers) ; en sortie : la liste des coordonnees des cases accessibles (tuples d'entiers)

        et avec leur contenu (porte ou vide) """

        casespossibles=[]

        x_voy=position[0]

        y_voy=position[1]

        for coord in [(x_voy-1, y_voy-1), (x_voy-1, y_voy), (x_voy-1, y_voy+1), (x_voy, y_voy-1), (x_voy, y_voy+1), (x_voy+1, y_voy-1),(x_voy+1, y_voy), (x_voy+1, y_voy+1)]:

            contenu = self.grille.getContenuCase(coord)

            if contenu[0]==None and contenu[1]==None: # case accessible

                casespossibles.append((coord, contenu[2]))               

        return casespossibles

            

        

    def seDeplacer(self):

        """ deplacement d'un voyageur. Sortie : nouvelle position du voyageur (tuple d'entiers).

        Le voyageur commence par observer les cases alentour et etablit ainsi une liste de possibilites.

        Si une des cases accessibles est une des etapes de son trajet, il y va. Sinon, on choisit celle le devie le moins possible de son trajet

        (produit scalaire de deux vecteurs) """

        maposition=self.grille.getPosition(self)

# ATT : manque un self
        casespossibles=self.autourVoyageur(maposition) 

        if casespossibles==[] : return(maposition) # aucune case accessible, le voyageur ne bouge pas

        else :

            maxi = -1

            for case in casespossibles:           #on parcourt la liste des cases accessibles
                
# ATT ; si la case est la 1ere porte du trajet du voyageur : if (case[1]))self.trajet[0]
                if case[1] == self.trajet[0] :       # la case est une porte du trajet du voyageur

                    self.trajet.pop(case[1]) # suppression de l'etape
                    
# ATT : ajout self. devant grille
                    if self.trajet ==[] : self.grille.deleteVoyageur(self) # le voyageur est arrive ; on le supprime de la grille

# QUESTION : dans ce cas la valeur de retour va-t-elle traitee ?
                    return case[0]

                else :

                    coord_etape=self.grille.getPosition(self.trajet[0]) # on recupere les coordonnees de la porte a atteindre                   

                    vecteur1=(coord_etape[0] - maposition[0], coord_etape[1] - maposition[1])

# ATT : A quoi correspond coord dans vecteur2 ? coord[0] par case[0][0]
                    vecteur2=(case[0][0] - maposition[0], case[0][1] - maposition[1])
# ATT : ajout de la biblio Math pour sqrt
                    cosinus = (vecteur1[0]*vecteur2[0] + vecteur1[1]*vecteur2[1])/(sqrt(vecteur1[0]**2 + vecteur1[1]**2)*sqrt(vecteur2[0]**2 + vecteur2[1]**2))

                    if cosinus >= maxi :

                        maxi = cosinus
# ATT : idem ci dessus : coord par case[0] 
                        new_pos=coord

            if maxi < 0 : return(maposition) # le voyageur est dans une situation ou il devrait reculer. Il ne bouge pas.

            return new_pos

    

    

class Obstacle:

    def __init__(self, couleur, grille):

        self.couleur = couleur

        self.grille = grille



class Porte:

    def __init__(self, couleur, grille):

        self.couleur = couleur

        self.grille = grille

        

