"""
Created on Wed Sep 23 15:02:28 2026
@author: Arnaud PAJANI - Ethan MAY
Jeu de casse-briques | classe Balle
A faire : Tout
"""

import random as rd
import math as ma

class Balle():
    def __init__(self, canvas,fenetre) -> None:
        self.rayon = 10
        self.coordX = 400
        self.coordY = 700
        self.couleur = "red"
        self.vitesse = 8
        self.angle = rd.uniform(ma.pi, 2*ma.pi) # commence en allant vers les briques
        self.DX = self.vitesse*ma.cos(self.angle)
        self.DY = self.vitesse*ma.sin(self.angle)
        self.affiche = canvas
        self.fenetre = fenetre
        self.nom = self.affiche.create_oval(self.coordX-self.rayon, self.coordY-self.rayon, self.coordX+self.rayon, self.coordY+self.rayon, fill=self.couleur)
        
    def mouvement(self,nouvX,nouvY):
        """
        entree : nouvX (int) / nouvY (int), nouvelle position de la balle
        sortie True / False, true si la balle est encore dans l'ecran
        
        """
        if (0 < nouvX and nouvX < 800) and (0 < nouvY and nouvY < 800):
            self.coordX = nouvX
            self.coordY = nouvY
            return True
        else : 
            return False
    
    def deplacement(self): # rebond sur les bords de l'ecran
    
        if self.coordX + self.rayon + self.DX > 790: # rebond à droite
            self.coordX = 2 * (800 - self.rayon) - self.coordX
            self.DX = -self.DX
        
        if self.coordX - self.rayon + self.DX < 10: # rebond à gauche
            self.coordX = 2 * self.rayon - self.coordX
            self.DX = -self.DX
        
        if self.coordY + self.rayon + self.DY > 790 : # rebond en bas
            self.coordY = 2 * (800 - self.rayon) - self.coordY
            self.DY = -self.DY
        
        if self.coordY - self.rayon + self.DY < 10: # rebond en haut
            self.coordY = 2 * self.rayon - self.coordY
            self.DY = -self.DY
        
        self.coordX = self.coordX+self.DX
        self.coordY = self.coordY+self.DY
        
        self.affiche.coords(self.nom,self.coordX-self.rayon,self.coordY-self.rayon,self.coordX+self.rayon,self.coordY+self.rayon) # affichage deplacement
        self.fenetre.after(20, self.deplacement)

