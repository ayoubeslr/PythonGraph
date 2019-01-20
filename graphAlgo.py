from graphCouleur import graphCouleur

class graphAlgo():
    def __init__(self):
        self.__sommet = []

    def __str__(self):
        return f"{self.__sommet}"

    def classerSommet(self, graphe):
        for i in range(graphe.length):
            tuple = graphe.liste[i]
            degG = graphe.degSommet(tuple[0])
            degD = graphe.degSommet(tuple[1])
            newtupleG = (degG, tuple[0])
            newtupleD = (degD, tuple[1])
            if newtupleG not in self.__sommet:
                self.__sommet.append(newtupleG)
            if newtupleD not in self.__sommet:
                self.__sommet.append(newtupleD)
            self.__sommet.sort()
            self.__sommet.reverse()
        return self

                
    def attribuerCouleur(self, graphe):
        couleurs = 0
        j = 0
        while len(self.__sommet) != 0:
            couleurs += 1
            liste = [self.__sommet[0]]
            i = len(self.__sommet) - j
            while i != 0:
                adjacent1 = graphe.adjacent(self.__sommet[0])
                tuple = self.__sommet[i-1]
                if tuple[1] not in adjacent1:
                    liste.append(tuple[1])
                    del tuple
                    j +=1
                i -= 1
                del self.__sommet[0]
                j += 1
        return liste
            
            


corps = graphCouleur()

corps.ajouter(0,0)
corps.ajouter(0,1)
corps.ajouter(0,3)
corps.ajouter(0,2)
corps.ajouter(2,3)
corps.ajouter(2,4)


print(corps)

print(corps.degSommet(0))
liste = graphAlgo()
print(liste.classerSommet(corps))
print(corps.adjacent(0))
print(liste.attribuerCouleur(corps))