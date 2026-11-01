#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 15:02:28 2026
@author: Arnaud PAJANI - Ethan MAY
Jeu de casse-briques | classe BriqueMobile
A faire : Tout
"""

from classes.briques.brique import Brique


class BriqueMobile(Brique):
    def __init__(self, pDurabilite = None, pPouvoir = None, pEffets = None, pMobile):
        # taille & durabilite sont herite de brique
        self.mobile = True
        self.tracer = pMobile # 2 coordonnees (haut gauche) entre lesquelles la brique se deplacera

