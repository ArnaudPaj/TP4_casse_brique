#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 15:02:28 2026
@author: Arnaud PAJANI - Ethan MAY
Jeu de casse briques | fichier tkinter
A faire : Tout
"""

import tkinter as tk

ecran = tk.Tk() # Create the main window
ecran.title("Casse brique")

### taille ecran ###
Jeu = tk.Canvas(ecran, width=800, height=800)
Jeu.pack()

vie = tk.StringVar(value="vie = 3")
afficheVie = tk.Label(Jeu, textvariable=vie, bg="black", fg="orange")
afficheVie.place(x=10, y=10)

score = tk.StringVar(value="score = 0")
afficheScore = tk.Label(Jeu, textvariable=score, bg="black", fg="orange")
afficheScore.place(x=700, y=10)



buttonQuit = tk.Button(ecran, text="Quitter", fg="red", command=ecran.destroy)
buttonQuit.pack()

ecran.mainloop() # execute la loop Tkinter