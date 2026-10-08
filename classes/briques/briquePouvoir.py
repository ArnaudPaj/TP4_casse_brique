"""
Created on Wed Sep 23 15:02:28 2026
@author: Arnaud PAJANI - Ethan MAY
Jeu de casse-briques | classe BriquePouvoir
A faire : Tout
"""

from classes.briques.brique import Brique


class BriquePouvoir(Brique):
    def __init__(self, pPouvoir, pEffets, pMobile) -> None:
        self.durabilite = 1
        self.taille = "TBD" # To Be Determined
        self.pouvoir = pPouvoir

