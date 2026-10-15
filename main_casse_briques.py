#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 15:02:28 2026
@author: Arnaud PAJANI - Ethan MAY
Jeu de casse briques | fichier tkinter
A faire : Tout
"""

import tkinter as tk
import classes.balle as ba
import classes.joueur as jo
from interface import Interface


class Main():
    """
    Constructeur de la partie
    """
    def __init__(self):
        self.interface= Interface()
        self.lBriques = []
        self.Joueur = jo.Joueur(self.interface.Jeu, self.interface.ecran)
        self.Balle = ba.Balle(self.interface.Jeu, self.interface.ecran)
        self.vie = 3
        self.score = 0
        self.niveau = 1
        self.immortel = False
        self.dif = 1 #Niveau de difficulté
        
        # bouton_nouvelle_partie = Button(self.interface.frame_menu, text = 'Nouvelle partie', font= 'ROGFonts-Regular', command = self.start)
        # bouton_nouvelle_partie.grid(row = 1, column = 0, padx = 15, pady = 15)
        # label_vie = Label(self.interface.frame_data, text = '', font= 'ROGFonts-Regular', background = '#555555')
        # label_vie.grid(row = 1, column = 0, padx = 15, pady = 15)
        # label_score = Label(self.interface.frame_data, text = '', font= 'ROGFonts-Regular', background = '#555555')
        # label_score.grid(row = 2, column = 0, padx = 15, pady = 15)
        
        self.interface.Jeu.focus_set() # Demander le focus pour que la fenêtre capture les touches
        self.interface.Jeu.bind("<KeyPress>", lambda event: self.Clavier(event))
        self.interface.ecran.mainloop() # execute la loop Tkinter

    def Clavier(self,event):
        '''
        Permet de déplacer le joueur et les autres interactions 
        '''
        touche_pressee = event.keysym
        if touche_pressee == 'Escape':
            self.interface.ecran.destroy()
            
        if touche_pressee == 'Left':
            self.Joueur.dep_gauche()
        
        if touche_pressee == 'Right':
            self.Joueur.dep_droit()
        
        if touche_pressee == 'i' :
            self.immortel = True
        
        if touche_pressee == 'm' :
            self.immortel = False
        
        if touche_pressee == 'n' :
            self.niveau +=1


