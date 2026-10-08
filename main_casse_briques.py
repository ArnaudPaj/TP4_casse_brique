#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 15:02:28 2026
@author: Arnaud PAJANI - Ethan MAY
Jeu de casse briques_ fichier tkinter
A faire : Tous
"""

import tkinter as tk

ecran = tk.Tk() # Create the main window
ecran.title("Casse brique")

### taille ecran ###
dimension = tk.Canvas(ecran, width=800, height=800)
dimension.pack()



buttonQuit = tk.Button(ecran, text="Quitter", fg="red", command=ecran.destroy)
buttonQuit.pack()

ecran.mainloop() # execute la loop Tkinter