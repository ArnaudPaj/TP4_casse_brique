#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 15:02:28 2026
@author: Arnaud PAJANI - Ethan MAY
Jeu de casse-briques | classe Balle
A faire : Tout
"""

import random as rd
import math as ma

class Balle():
    def __init__(self, canvas, fenetre, joueur) -> None:
        self.rayon = 10
        self.coordX = 500 # X du centre
        self.coordY = 900 # Y du centre
        self.couleur = "red"
        self.vitesse = 4
        self.angle = rd.uniform(5/4*ma.pi, 7/4*ma.pi) # commence en allant vers les briques
        self.DX = self.vitesse*ma.cos(self.angle)
        self.DY = self.vitesse*ma.sin(self.angle)
        self.affiche = canvas
        self.fenetre = fenetre
        self.joueur = joueur
        self.dep = False
        self.nom = self.affiche.create_oval(self.coordX-self.rayon, self.coordY-self.rayon, self.coordX+self.rayon, self.coordY+self.rayon, fill=self.couleur)
        self.affiche.update()  # actualise le canvas
        
        
    def position(self):
        return self.coordX,self.coordY
    
    def placeBalle(self):
        """ Reset des donnees de la balle """
        self.coordX = 500 # X du centre
        self.coordY = 900 # Y du centre
        """ deplace la balle """
        self.affiche.coords(self.nom, self.coordX-self.rayon, self.coordY-self.rayon, self.coordX+self.rayon, self.coordY + self.rayon)
        self.affiche.update()  # actualise le canvas
        
    def deplacement(self):
        """
        entree : None
        sortie True / False, true si la balle est encore dans l'ecran
        
        """
        self.coordX += self.DX
        self.coordY += self.DY
        self.rebondMurs()
        if self.estCollisionJoueur():
            self.rebondJoueur()
        self.affichage()
        if self.dep:
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
        if self.coordY + self.rayon + self.DY > 950 : 
            self.coordY = 2 * (960 - self.rayon) - self.coordY
            self.DY = -self.DY
        self.coordX += self.DX
        self.coordY += self.DY
        
    def rebondBrique(self):
        self.coordX += self.DX
        self.coordY += self.DY
            
        
    def affichage(self):
        self.affiche.coords(self.nom, self.coordX-self.rayon, self.coordY-self.rayon, self.coordX+self.rayon, self.coordY + self.rayon) # affichage deplacement
        self.affiche.update()  # actualise le canvas


    def estCollisionJoueur(self):
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

    def estCollisionBrique(self, brique):
        pass
