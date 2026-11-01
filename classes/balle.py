#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 15:02:28 2026
@author: Arnaud PAJANI - Ethan MAY
Jeu de casse-briques | classe Balle
A faire : Tout
"""
import math as ma
import random as ran

class Balle:
    def __init__(self, canvas):
        self.rayon = 10
        self.coordX = 500 # X du centre
        self.coordY = 900 # Y du centre
        self.canvas = canvas
        self.dx = 4
        self.dy = -4
        self.vitesse = 6
        self.nom = self.canvas.create_oval(self.coordX-self.rayon, self.coordY-self.rayon, self.coordX+self.rayon, self.coordY+self.rayon,fill="red")

    def affiche(self):
        self.canvas.update()  # actualise le canvas
        
    def deplacement(self):
        self.canvas.move(self.nom, self.dx, self.dy)
        self.canvas.update()  # actualise le canvas
        
    def position(self):
        # return self.coordX,self.coordY ou
        return self.canvas.coords(self.nom)

    def rebonfHorizontal(self):
        self.dx = -self.dx

    def rebondVertical(self):
        self.dy = -self.dy

    def reset(self): # ancien placeBalle
        """Replace la balle au-dessus de la raquette."""
        self.canvas.coords(self.nom, 500-self.rayon, 900-self.rayon, 500+self.rayon, 900+self.rayon)
        angle = ran.uniform(ma.pi, 2*ma.pi)
        self.dx = self.vitesse*ma.cos(angle)
        self.dy = self.vitesse*ma.sin(angle)
    
    """ Passe dans le main -> plus propre et aiser pour le reste
    def deplacement(self):
        self.coordX += self.DX
        self.coordY += self.DY
        self.rebondMurs()
        
        if self.estCollisionJoueur(self.joueur):
            self.rebondJoueur()

        if self.estCollisionBrique():
             self.rebondBrique()    

        if self.coordY > 1080:
            self.dep = False
            # supprime la balle
            # retire une vie
            # remet la balle au centre
            # attend un espace
            
        if self.dep:
            self.affichage()
            self.fenetre.after(25, self.deplacement)
    
    def rebondMurs(self): # rebond sur les bords de l'ecran
    
        if self.coordX + self.rayon + self.DX > 950: # rebond à droite
            self.coordX = 2 * (960 - self.rayon) - self.coordX
            self.DX = -self.DX
        
        if self.coordX - self.rayon + self.DX < 10: # rebond à gauche
            self.coordX = 2 * self.rayon - self.coordX
            self.DX = -self.DX
        
        if self.coordY - self.rayon + self.DY < 10: # rebond en haut
            self.coordY = 2 * self.rayon - self.coordY
            self.DY = -self.DY
            
        # Conditione de perte de vie voir defaite // Rebond en bas
        # if self.coordY + self.rayon + self.DY > 950 : 
        #     self.coordY = 2 * (960 - self.rayon) - self.coordY
        #     self.DY = -self.DY
        
        self.coordX += self.DX
        self.coordY += self.DY

    def rebondJoueur(self):
        self.DY = -self.DY
        self.coordX += self.DX
        self.coordY += self.DY
        
    def rebondBrique(self):
        self.DY = -self.DY
        self.coordX += self.DX
        self.coordY += self.DY

    def estCollisionJoueur(self, joueur):
        joueurCoordX1 = self.joueur.coordX
        joueurCoordX2 = self.joueur.coordX + 100
        joueurCoordY1 = self.joueur.coordY
        joueurCoordY2 = self.joueur.coordY + 20
        valRen = False
        px = max(joueurCoordX1, min(self.coordX, joueurCoordX2)) # point le plus proche du cercle, dans le rectangle
        py = max(joueurCoordY1, min(self.coordY, joueurCoordY2)) # idem pour Y

        distCarre = (self.coordX-px) ** 2 + (self.coordY-py) ** 2 # distance euclidienne entre balle et rectangle
        if distCarre <= self.rayon ** 2:
            valRen = True 
        return valRen

    def estCollisionBrique(self):
        valRen = False
        print(lBriques)
        # briqueX1, briqueY1, briqueX2, briqueY2 = self.canvas.coords(brique) # coordonnées en haut à gauche, et en bas à droite de la brique
        # balleX1, balleY1, balleX2, balleY2 = self.canvas.coords(self) # Idem pour l'ellipse (le cercle)
        
        # if (briqueX1 < balleX2 and briqueX2 > balleX1 and briqueY1 < balleY2 and briqueY2 > balleY1):
        #     valRen = True 
        return valRen
    
    """

