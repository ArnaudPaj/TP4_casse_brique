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
        self.coordX = 200
        self.coordY = 700
        self.couleur = "blue"
        self.vitesse = 10
        self.affiche = canvas
        self.fenetre = fenetre
        self.nom = self.affiche.create_oval(self.coordX*2-self.rayon, self.coordY-self.rayon, self.coordX+self.rayon, self.coordY+self.rayon, fill=self.couleur)