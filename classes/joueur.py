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
        self.coordX = [350,450]
        self.coordY = [740,760]
        self.couleur = "blue"
        self.vitesse = 10
        self.affiche = canvas
        self.fenetre = fenetre
        self.nom = self.affiche.create_rectangle(self.coordX[0], self.coordY[0], self.coordX[1], self.coordY[1], fill=self.couleur) # 100*20 px