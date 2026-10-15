#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 12:05:05 2026
@author: Arnaud PAJANI - Ethan MAY
Jeu de casse briques | class joueur
A faire : Tout
"""

class Joueur():
    def __init__(self,canvas,fenetre):
        self.rayon = 10
        self.coordX = 450 # (Origine) coin haut à gauche
        self.coordY = 940 # (Origine) coin haut à droite
        self.couleur = "blue"
        self.vitesse = 10
        self.canvas = canvas
        self.fenetre = fenetre
        self.nom = self.canvas.create_rectangle(self.coordX, self.coordY, self.coordX+100, self.coordY+20, fill=self.couleur) # 100*20 px 
        
# ============================ Mouvement ======================== #
    def dep_gauche(self):
        if self.coordX > 11:
            self.coordX -= self.vitesse
            self.affiche()
        
    def dep_droit(self):
        if self.coordX < 971:
            self.coordX += self.vitesse
            self.affiche()
            
    def affiche(self):
        self.canvas.moveto(self.nom, self.coordX, self.coordY) # Nouveau deplacement
        self.canvas.update()  # actualise le canvas
        
# ======================= gestion de la vie ===================== #
    def immortalite(self):
        self.vie = -1 # correspond à l'immortalite
        
    def perdeVie(self):
        self.vie -= 1
        
# ============================ Score  =========================== #
    def touche(self):
        self.score += 10
        