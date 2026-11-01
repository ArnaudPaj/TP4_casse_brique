#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 15:02:28 2026
@author: Arnaud PAJANI - Ethan MAY
Jeu de casse-briques | classe BriqueDur
A faire : Tout
"""


"""
########## HERITIER DE BRIQUE ##########

Propriétés de la classe:
- taille


Méthodes:

"""

from classes.briques.brique import Brique


class BriqueDur(Brique):
    def __init__(self, pDurabilite, pPouvoir = None, pEffets = None, pMobile = None):
        # taille est herite de brique
        self.durabilite = pDurabilite
        
    def hit(self):
        """Retire un point de résistance."""
        self.durabilite -= 1

        if self.durabilite <= 0:
            self.destroy()
            return True

        self.canvas.itemconfig(self.nom, fill=self.COLORS.get(self.durabilite, "#9b5de5"))
        self.canvas.itemconfig(self.label, text=str(self.durabilite if self.durabilite > 1 else "")
        return False

