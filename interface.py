#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 09:22:07 2026
@author: Arnaud PAJANI - Ethan MAY
interfasse pour le casse briques | fichier tkinter
A faire : Tout
"""

import tkinter as tk

class Interface():
    def __init__(self):
        self.ecran = tk.Tk() # Create the main window
        self.ecran.title("Casse brique")
        self.ecran.geometry("1920x1080") #You want the size of the app to be 1920x1080

        ### taille de la partie ou on joue ###
        self.Jeu = tk.Canvas(self.ecran, width=1000, height=1000, bg="black")
        self.Jeu.pack(side="right")
        
        buttonQuit = tk.Button(self.ecran, text="Quitter", fg="red", command=self.ecran.destroy)
        buttonQuit.pack(side = 'left')