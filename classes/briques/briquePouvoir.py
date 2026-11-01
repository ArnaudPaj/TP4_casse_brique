#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 15:02:28 2026
@author: Arnaud PAJANI - Ethan MAY
Jeu de casse-briques | classe BriquePouvoir
A faire : Tout
"""

from classes.briques.brique import Brique


class BriquePouvoir(Brique):
    def __init__(self, pPouvoir, pEffets, pMobile):
        # taille est herite de brique
        self.durabilite = 1
        self.pouvoir = pPouvoir

