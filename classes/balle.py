"""
Created on Wed Sep 23 15:02:28 2026
@author: Arnaud PAJANI - Ethan MAY
Jeu de casse-briques | classe Balle
A faire : Tout
"""

class Balle():
    def __init__(self) -> None:
        self.rayon = 10
        self.coordX = 400
        self.coordY = 400
        
    def mouvement(self,nouvX,nouvY):
        """
        entree : nouvX (int) / nouvY (int), nouvelle position de la balle
        sortie True / False, true si la balle est encore dans l'ecran
        
        """
        if (0 < nouvX and nouvX < 800) and (0 < nouvY and nouvY < 800):
            self.coordX = nouvX
            self.coordY = nouvY
            return True
        else : 
            return False