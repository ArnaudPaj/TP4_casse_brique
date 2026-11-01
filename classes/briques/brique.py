#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 15:02:28 2026
@author: Arnaud PAJANI - Ethan MAY
Jeu de casse-briques | classe Brique
A faire : Tout
"""


class Brique():
    def __init__(self, pCoordX, pCoordY, canvas):
        self.durabilite = 1
        self.vivant = True
        self.coordX = pCoordX 
        self.coordY = pCoordY
        self.canvas = canvas
        self.nom = self.canvas.create_rectangle(self.coordX, self.coordY, self.coordX+60, self.coordY+30, fill="firebrick4", outline="black", width=2) # 60*30 px
        self.canvas.update()  # actualise le canvas

# ====================== VIE ===================== #
    def estVivant(self):
        """
            Entrée(s) : -
            Sortie(s) : True/False (bool)
            Algo : 
        """
        return self.vivant
    
    def touche(self):
        """Retire un point de résistance."""
        self.durabilite -= 1
        if self.durabilite <= 0:
            self.detruit()
            return True
        self.canvas.itemconfig(self.nom,fill=self.COLORS.get(self.durabilite, "#9b5de5"))
        self.canvas.itemconfig(self.label,text=str(self.durabilite) if self.durabilite > 1 else "")
        return False
    
    def detruit(self):
        if self.durabilite == 0:
            self.canvas.delete(self.nom)
            self.canvas.update()
            self.vivant = False
            
# ====================== COLLISIONS ===================== #

    def position(self):
        return self.coordX, self.coordY, self.coordX+60, self.coordY+30
        # ou return self.canvas.coords(self.id)
    
      
""" Geree dans le main
    def EstCollisionBalle(self, balle):
        
            Entrée(s) : la balle
            Sortie(s) : True/False (Bool)
            Algo : Collision balle/brique
        
        valRen = False
        # travailler avec les dimensions
        # où est-ce qu'on prend notre origine ?

        briqueX1, briqueY1, briqueX2, briqueY2 = self.canvas.coords(self) # coordonnées en haut à gauche, et en bas à droite de la brique
        balleX1, balleY1, balleX2, balleY2 = self.canvas.coords(balle) # Idem pour l'ellipse (le cercle)
        if (briqueX1 < balleX2 and briqueX2 > balleX1 and briqueY1 < balleY2 and briqueY2 > balleY1):
            valRen = True

        return valRen
"""














    