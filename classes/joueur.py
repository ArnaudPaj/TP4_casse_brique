#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 12:05:05 2026
@author: Arnaud PAJANI - Ethan MAY
Jeu de casse briques | class joueur
A faire : Tout
"""

class Joueur():
    def __init__(self,canvas):
        self.coordX = 450 # (Origine) coin haut à gauche
        self.coordY = 990 # (Origine) coin haut à droite
        self.couleur = "blue"
        self.vitesse = 16
        self.canvas = canvas
        self.nom = self.canvas.create_rectangle(self.coordX, self.coordY, self.coordX+100, self.coordY+20, fill=self.couleur, outline='black') # 100*20 px 
        
# ======================== Mouvement/Position =================== #
    def dep_gauche(self):
        if self.coordX > 11:
            self.coordX -= self.vitesse
            self.affiche()
        
    def dep_droit(self):
        if self.coordX < 851:
            self.coordX += self.vitesse
            self.affiche()
            
    def affiche(self):
        self.canvas.moveto(self.nom, self.coordX, self.coordY) # Nouveau deplacement
        self.canvas.update()  # actualise le canvas
        
    def position(self):
        return self.coordX,self.coordY,self.coordX+100,self.coordY+20
    
    def reset(self):        
        self.coordX = 450 # X du centre
        self.coordY = 990 # Y du centre
        self.affiche()

# en théorie passe dans le main -> gestion plus simple
# ======================= gestion de la vie ===================== #
    def immortalite(self):
        self.vie = -1 # correspond à l'immortalite
        
    def perdeVie(self):
        self.vie -= 1
        
# ============================ Score  =========================== #
    def touche(self):
        self.score += 50
        
