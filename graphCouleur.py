class graphCouleur():
    def __init__(self):
        self.liste = []
        self.length = 0
    
    def __str__(self):
        return f"{self.liste}"
    
    
    def ajouter(self, som1, som2):
        tuple = (som1, som2)
        self.liste.append(tuple)
        self.length += 1
    
    def degSommet(self, sommet):
        deg = 0
        for i in range(len(self.liste)):
            tuple = self.liste[i]
            if tuple[0] == sommet or tuple[1] == sommet:
                deg += 1
        return deg
    
    def adjacent(self, sommet):
        liste = []
        for i in range(len(self.liste)):
            tuple = self.liste[i]
            if tuple[0] == sommet:
                liste.append(tuple[1])
            if tuple[1] == sommet:
                liste.append(tuple[0])
        return liste
    
    
        
    
    
    
            
            

