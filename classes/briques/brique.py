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
- position

Méthodes:

########## Autrement dit...
De quelles données avons-nous besoin concernant la brique ?
Quels opérations imposer à la brique ?
##########

- getDurabilite
- getPosition
- supprimerBrique
- estTouchee

"""

class Brique():
    def __init__(self, pDurabilite, pTaille, pPositionX, pPositionY) -> None:
        self.durabilite = 1
        self.taille = "TBD" # To Be Determined
        self.positionX = pPositionX
        self.positionY = pPositionY



    def getDurabilite(self):
        """
            Entrée(s) : -
            Sortie(s) : durabilité (int)
            Algo : 
        """
        pass

    def getPositionX(self):
        """
            Entrée(s) : 
            Sortie(s) : 
            Algo : 
        """
        pass

    def getPositionY(self):
        """
            Entrée(s) : 
            Sortie(s) : 
            Algo : 
        """
        pass

    def supprimerBrique(self):
        """
            Entrée(s) : -
            Sortie(s) : 
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