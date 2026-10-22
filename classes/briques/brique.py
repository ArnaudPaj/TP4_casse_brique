#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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
                       "largeur":20} # en dur
        self.coordX = pCoordX 
        self.coordY = pCoordY
        self.couleur = "white"  # code en dur
        self.canvas = canvas
        self.fenetre = fenetre
        self.nom = self.canvas.create_rectangle(self.coordX, self.coordY, self.coordX+60, self.coordY+20, fill=self.couleur) # 60*20 px
        self.canvas.update()  # actualise le canvas

# ====================== VIE ===================== #
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

    def position(self):
        return self.coordX,self.coordY
        
# Pour les copier/coller en respectant les bonnes pratiques 
# def BonnesPratiques():
#         """
#             Entrée(s) : 
#             Sortie(s) :
#             Algo : 
#         """