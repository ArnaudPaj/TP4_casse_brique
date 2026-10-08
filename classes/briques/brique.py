"""
Created on Wed Sep 23 15:02:28 2026
@author: Arnaud PAJANI - Ethan MAY
Jeu de casse-briques | classe Brique
A faire : Tout
"""


"""
########## CLASSE PARENT ##########

Propriétés de la classe:
- taille
- durabilité (aussi, dureté)
- coord

Méthodes:

########## Autrement dit...
De quelles données avons-nous besoin concernant la brique ?
Quels opérations imposer à la brique ?
##########

- obtenirDurabilite
- obtenirCoord(X/Y) (2 fonctions)
- estTouchee
"""

class Brique():
    def __init__(self, pDurabilite, pTaille, pCoordX, pCoordY) -> None:
        self.durabilite = 1
        self.taille = "TBD" # To Be Determined
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

    def obtenirCoordX(self):
        """
            Entrée(s) : -
            Sortie(s) : coordX (int)
            Algo : 
        """
        pass

    def obtenirCoordY(self):
        """
            Entrée(s) : -
            Sortie(s) : coordY (int)
            Algo : 
        """
        pass

    def estTouchee(self):
        """
            Entrée(s) : -
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