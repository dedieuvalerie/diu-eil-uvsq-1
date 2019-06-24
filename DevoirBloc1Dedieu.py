from math import *
import random


class Point:
    def __init__(self, x, y):
        self.abscisse=x
        self.ordonnee =y
    
    def getX(self):
        return self.abscisse
    
    def getY(self):
        return self.ordonnee

class Cercle:
    def __init__(self, c, r):
        self.centre=c
        self.rayon=r
    
    def centreCercle(self):
        return self.centre
    
    def rayonCercle(self):
        return self.rayon
    
    def texte(self):
        chaine="cercle(("+str(self.centre.getX())+","+str(self.centre.getY())+") , "+ str(self.rayon)+")"
        print (chaine)

    def circonference(self):
        return 2*pi*self.rayon

    def deplace(self,dx,dy):
        self.centre=Point(self.centre.getX()+dx,self.centre.getY()+dy)


    def intersecteAvec(self,cercle2):  
        x2=cercle2.centreCercle().getX()
        y2=cercle2.centreCercle().getY()
        r2=cercle2.rayonCercle()
        sqdistX=(self.centre.getX()-x2)**2
        sqdistY=(self.centre.getY()-y2)**2
        distance=sqrt(sqdistX+sqdistY)
        return self.rayon +  r2 >= distance

    

    
   
#-------------------------- tests --------------------
m=Point(1,2)
c=Cercle(m,3)
c.texte()

centre=c.centreCercle()

r=c.rayonCercle()
print(r)

c.deplace(3,6)
c.texte()

m=Point(3,7)
c2=Cercle(m, 5)
c2.texte()
print(c.intersecteAvec(c2))



#--------------------------------------------------------

listeCercles=[]
for i in range(10):
    centre=Point(random.randint(1,20),random.randint(1,20))
    r=random.randint(1,10)
    c=Cercle(centre,r)
    listeCercles.append(c)

for c in listeCercles :
    c.texte()
    
dirCercles=[]

for cercle in listeCercles :
    dirCercles.append((cercle, [c for c in listeCercles if c!=cercle and cercle.intersecteAvec(c)]))
    
    
