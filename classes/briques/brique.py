"""
Created on Wed Sep 23 15:02:28 2026
@author: Arnaud PAJANI - Ethan MAY
Jeu de casse-briques | classe Brique
A faire : Tout
"""



class Brique():
    def __init__(self, pLongueur, pLargeur, pCoordX, pCoordY, canvas, fenetre) -> None:
        self.durabilite = 1
        self.taille = {"longueur":pLongueur,
                       "largeur":pLargeur} # To Be Determined
        self.coordX = pCoordX 
        self.coordY = pCoordY
        # deux lignes qui suivent sont en dur
        self.coordX = 100
        self.coordY = 200
        self.couleur = "white"  # code en dur
        self.canvas = canvas
        self.fenetre = fenetre
        self.nom = self.canvas.create_rectangle(self.coordX, self.coordY, self.coordX+60, self.coordY+30, fill=self.couleur) # 60*30 px
        self.canvas.update()  # actualise le canvas

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

        if True:
            pass

        return valRen


def BonnesPratiques():
        """
            Entrée(s) : 
            Sortie(s) :
            Algo : 
        """