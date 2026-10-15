"""
Created on Wed Sep 23 15:02:28 2026
@author: Arnaud PAJANI - Ethan MAY
Jeu de casse-briques | classe Brique
A faire : Tout
"""


class Brique():
    def __init__(self, pCoordX, pCoordY, canvas, fenetre) -> None:
        self.durabilite = 1
        self.taille = {"longueur":60,
                       "largeur":30} # en dur
        self.coordX = pCoordX 
        self.coordY = pCoordY
        # deux lignes qui suivent sont en dur
        self.coordX = 100
        self.coordY = 200
        self.couleur = "black"  # code en dur
        self.canvas = canvas
        self.fenetre = fenetre
        self.nom = self.canvas.create_rectangle(self.coordX, self.coordY, self.coordX+60, self.coordY+30, fill=self.couleur) # 60*30 px

# ====================== VIE ===================== #
    def obtenirDurabilite(self):
        """
            Entrée(s) : -
            Sortie(s) : durabilité (int)
            Algo : 
        """
        return self.durabilite

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

# ====================== COLLISIONS ===================== #
    def EstCollisionBalle(self, balle):
        """
            Entrée(s) : Collision balle/brique
            Sortie(s) : True/False (Bool)
            Algo : 
        """
        valRen = False
        # travailler avec les dimensions
        # où est-ce qu'on prend notre origine ?

        briqueX1, briqueY1, briqueX2, briqueY2 = self.canvas.coords(self)
        balleX1, balleY1, balleX2, balleY2 = self.canvas.coords(balle)
        if (briqueX1 < balleX2 and briqueX2 > balleX1 and briqueY1 < balleY2 and briqueY2 > balleY1):
            valRen = True

        return valRen


def BonnesPratiques():
        """
            Entrée(s) : 
            Sortie(s) :
            Algo : 
        """