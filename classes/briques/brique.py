"""
Created on Wed Sep 23 15:02:28 2026
@author: Arnaud PAJANI - Ethan MAY
Jeu de casse-briques | classe Brique
A faire : Tout
"""


class Brique():
    def __init__(self, pLongueur, pLargeur, pCoordX, pCoordY) -> None:
        self.durabilite = 1
        self.taille = {"longueur":pLongueur,
                       "largeur":pLargeur} # To Be Determined
        self.coordX = pCoordX
        self.coordY = pCoordY


    def obtenirDurabilite(self):
        """
            Entrée(s) : -
            Sortie(s) : durabilité (int)
            Algo : 
        """
        return self.durabilite
        pass

    def estVivant(self):
        """
            Entrée(s) : -
            Sortie(s) : True/False (bool)
            Algo : 
        """
        valRen = False
        if self.obtenirDurabilite() != 0:
             valRen = True
        return valRen

    def obtenirCoordX(self):
        """
            Entrée(s) : -
            Sortie(s) : coordX (int)
            Algo : 
        """
        return self.coordX
        pass

    def obtenirCoordY(self):
        """
            Entrée(s) : -
            Sortie(s) : coordY (int)
            Algo : 
        """
        return self.coordY
        pass

    def estTouchee(self):
        """
            Entrée(s) : Collision balle/brique
            Sortie(s) : True/False (Bool)
            Algo : 
        """
        pass


def BonnesPratiques():
        """
            Entrée(s) : 
            Sortie(s) :
            Algo : 
        """