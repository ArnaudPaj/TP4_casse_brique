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
    def __init__(self, pNumero, motif, canvas, fenetre) -> None:
        self.numero = pNumero # sera constante par instance
        self.NombreBriqueMax = 16*4 # codé en dur, nb max de briques sur l'ecran
        self.NombreBriqueParLigne = 960 // 60 # codé en dur, se référer à la taille d'une brique (normalisé)
        self.NombreColonnes = self.NombreBriqueMax // self.NombreBriqueParLigne
        self.NombreBriqueApparaitre = self.NombreBriqueMax # alias pour NombreBriqueMax
        self.motif = "classique" # codé en dur "classique", voir d'autres types
        self.canvas = canvas
        self.fenetre = fenetre
        self.briques = self.genererBriques() # instancie classe brique dans une liste, il y a NombreBriqueMax éléments dans la liste
                
        # self.tailleX = 3
        # self.tailleY = 1

    def estGagne(self):
        """
            Entrée(s) : -
            Sortie(s) : True/False (bool)
            Algo :
        """

        valRen = True
        briquesRestantes = self.obtenirBriquesRestantes()

        for brique in briquesRestantes:
            if brique.estVivant():
                valRen = False

        return valRen

    def genererBriques(self): # génère les briques dans une liste et les fait apparaitre
        """
            Entrée(s) : -
            Sortie(s) : -
            Algo :
        """

        """valRen = []
        instances = [Brique(80*i, 20*i, self.canvas, self.fenetre) for i in range(self.NombreBriqueApparaitre)] # dimensions en dur, à changer 
        valRen = instances"""

        valRen = []
        briqueModele = br.Brique(0, 0, self.canvas, self.fenetre)
        print(self.motif)
        if self.motif == "classique":
            # on va parcourir la liste comme une matrice
            for i in range(self.NombreColonnes):
                valRen.append([]) # Crée une colonne popur chaque boucle i
                for j in range(self.NombreBriqueParLigne):
                    brique = br.Brique(pCoordX=0+(j+briqueModele.taille["longueur"]), pCoordY=0+(i*briqueModele.taille["largeur"]), canvas=self.canvas, fenetre=self.fenetre)
                    valRen[i].append(brique) # On append dans la colonne correspondante
        
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

# def test2():
#     niveau = Niveau(1, "classique", "Hello", "gg")
#     res = niveau.genererBriques()
#     print(res)
#     print(len(res))

# test2()