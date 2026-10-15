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

ecran = tk.Tk() # Create the main window
ecran.title("Casse brique")
ecran.geometry("1920x1080") #You want the size of the app to be 500x500

### taille ecran ###
Jeu = tk.Canvas(ecran, width=1000, height=1000, bg="black")
Jeu.pack()
Jeu.focus_set() # Demander le focus pour que la fenêtre capture les touches

vie = tk.StringVar(value="vie = 3")
afficheVie = tk.Label(Jeu, textvariable=vie, bg="black", fg="orange")
afficheVie.place(x=10, y=10)

score = tk.StringVar(value="score = 0")
afficheScore = tk.Label(Jeu, textvariable=score, bg="black", fg="orange")
afficheScore.place(x=900, y=10)

balle = ba.Balle(Jeu,ecran)
balle.deplacement()

joueur = jo.Joueur(Jeu, ecran)

Jeu.bind("<KeyPress>", lambda event: joueur.keyPress(event))
Jeu.bind("<Escape>", lambda event: ecran.destroy())

buttonQuit = tk.Button(ecran, text="Quitter", fg="red", command=ecran.destroy)
buttonQuit.pack()

ecran.mainloop() # execute la loop Tkinter