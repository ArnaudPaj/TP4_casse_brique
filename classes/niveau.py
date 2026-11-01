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
    def __init__(self, pNumero, motif, canvas):
        self.numero = pNumero # sera constante par instance
        self.NombreBriqueMax = 16*8 # codé en dur, nb max de briques sur l'ecran
        self.NombreBriqueParLigne = 960 // 60 # codé en dur, se référer à la taille d'une brique (normalisé)
        self.NombreLigne = self.NombreBriqueMax // self.NombreBriqueParLigne
        self.NombreBriqueApparaitre = self.NombreBriqueMax # alias pour NombreBriqueMax
        self.motif = "classique" # codé en dur "classique", voir d'autres types
        self.canvas = canvas

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
        valRen = []
        n = 0
        if self.motif == "classique":
            # on va parcourir la liste comme une matrice
            if self.numero+4 <= self.NombreLigne:
                 n = self.numero+4
            for i in range(n):
                valRen.append([]) # Crée une colonne popur chaque boucle i
                for j in range(self.NombreBriqueParLigne):
                    brique = br.Brique(pCoordX=(j*60), pCoordY=30+2*((i+1)*5)+(i*30), canvas=self.canvas) # brique de 60*30 px
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
