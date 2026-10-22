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
import classes.niveau as ni
import classes.briques.brique as br

class Main():
    """
    Constructeur de la partie
    """
    def __init__(self):
        self.ecran = tk.Tk() # Create the main window
        self.ecran.title("Casse brique")
        self.ecran.geometry("1920x1080") #You want the size of the app to be 1920x1080

        ### canvas ou on joue ###
        self.Jeu = tk.Canvas(self.ecran, width=960, height=1080, bg="black")
        self.Jeu.pack(side="right")
        
        ### canvas des paramètres ###
        self.Data = tk.Canvas(self.ecran, width=960, height=1080)
        self.Data.pack(side="left")
        
        ### Donnee pour le jeu ###
        self.partie = False # statut de la partie (true pour commencee, false sinon)
        self.lBriques = []
        self.Joueur = jo.Joueur(self.Jeu, self.ecran)
        self.dejaBalle = False
        self.Balle = ba.Balle(self.Jeu, self.ecran, self.Joueur)
        self.vie = 3
        self.score = 0
        self.immortel = False
        self.dif = 1 #Niveau de difficulté
        self.niveau = ni.Niveau(self.dif, "classique", self.Jeu, self.ecran) # ID du niveau
        
        label_vie = tk.Label(self.Data, text = 'vie : 3', font= 'ROGFonts-Regular')
        label_vie.place(x=0,y=0)
        label_score = tk.Label(self.Data, text = 'score : 0', font= 'ROGFonts-Regular')
        label_score.place(x=820,y=0)
        boutonPartie = tk.Button(self.Data, text ='Nouvelle partie', font= 'ROGFonts-Regular', fg="green", command = self.start)
        boutonPartie.place(x=415,y=1000)
        #boutonPartie.place(x=415,y=500) # pour test Ethan
        buttonQuitte = tk.Button(self.Data, text="Quitter", font= 'ROGFonts-Regular', fg="red", command=self.ecran.destroy)
        buttonQuitte.place(x=450,y=1040)
        
        self.Jeu.focus_set() # Demander le focus pour que la fenêtre capture les touches
        self.Jeu.bind("<KeyPress>", lambda event: self.clavier(event))
        self.ecran.mainloop() # execute la loop Tkinter

    def clavier(self,event):
        '''
        Permet de déplacer le joueur et les autres interactions 
        '''
        touche_pressee = event.keysym
        if touche_pressee == 'Escape':
            self.ecran.destroy()
            
        if touche_pressee == 'Left':
            self.Joueur.dep_gauche()
            
        if touche_pressee == 'Right':
            self.Joueur.dep_droit()
            
        if touche_pressee == 'space':
            if self.partie:
                print("Start casse brique")
                self.Balle.placeBalle()
                self.Balle.deplacement()
                print("partie started")
                print("DX :", self.Balle.DX)
                print("DY :", self.Balle.DY)
                print("Vitesse :", self.Balle.vitesse)
            else:
                # jeu nb rebonds
                print("Start keep the ball")
                self.Joueur.placeJoueur()
                self.Balle.placeBalle()
                self.dejaBalle = True
                self.Balle.dep = True
                print("dep = Vrai")
                self.partie = False
                self.Balle.deplacement()
                
        if touche_pressee == 'i' :
            self.immortel = True
        
        if touche_pressee == 'm' :
            self.immortel = False
        
        """ if touche_pressee == 'n' :
            self.niveau += 1 """

    def start(self):
        """
        appel -> pas lance la balle (condition press espace)
                 affiche : espace pour commencer et mettre en pause la partie
                 genere les briques sur le terrain
        """
        # pour test 
        self.partie = True
        self.lBriques = self.niveau.briques
        #print("self.briques", self.niveau.briques)

    def gameStatus(self):
        while perdu != True:
            if self.Balle.dep:
                self.Balle.affichage()
                self.fenetre.after(25, self.deplacement)
            if self.vie == 0 :
                self.perdu
    
    def Perdu(self):
        pass

    def jouer(self):
        self.start()
        print(self.lBriques)
