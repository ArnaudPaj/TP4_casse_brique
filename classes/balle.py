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
