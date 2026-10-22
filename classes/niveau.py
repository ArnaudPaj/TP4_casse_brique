#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 15:02:28 2026
@author: Arnaud PAJANI - Ethan MAY
Jeu de casse-briques | classe Niveau
A faire : Tout
"""

import classes.briques.brique as br

class Niveau():
    def __init__(self, pNumero) -> None:
        self.numero = pNumero # sera constante par instance
        self.NombreBriqueMax = 25
        self.briques = self.apparaitreBriques()
        self.tailleX = 3
        self.tailleY = 1

    def estGagne(self):
        """
            Entrée(s) : -
            Sortie(s) : True/False (bool)
            Algo :
        """
        valRen = True
        briquesRestantes = self.obtenirBriquesRestantes(self.briques)

        for brique in briquesRestantes:
            if brique.estVivant():
                valRen = False

        return valRen

    def obtenirNombreBriqueApparaitre(self): # fonction superflue ?
        return self.NombreBriqueApparaitre

    def apparaitreBriques(self):
        """
            Entrée(s) : -
            Sortie(s) : -
            Algo :
        """

        valRen = []
        instances = [Brique(80*i, 20*i, self.canvas, self.fenetre) for i in range(self.NombreBriqueApparaitre)] # dimensions en dur, à changer 
        valRen = instances
        
        return valRen

    def obtenirBriquesRestantes(self):
        """
            Entrée(s) : liste des briques (obj) et statut (int) - (list)
            Sortie(s) : briques restantes (list)
            Algo : 
        """

        liste = self.briques.copy()
        valRen = []
        
        for brique in liste:
            if brique.estVivant():
                valRen.append(brique)

        return valRen

    def obtenirNombreBriquesRestantes(self):
        """
            Entrée(s) : -
            Sortie(s) : briques restantes (int)
            Algo : 
        """
        return len(self.briques)



# def test():
#     niveau = Niveau(1, 1)
#     briques = niveau.obtenirBriquesRestantes(niveau.briques)
#     print(briques)
#     print(niveau.obtenirNombreBriquesRestantes(briques), "brique restante")
#     print("\n\n\n")
#     print("Gagné =", niveau.estGagne())
#     briques[0].durabilite = 0
#     print("Gagné =",niveau.estGagne(), "après modif")

# test()