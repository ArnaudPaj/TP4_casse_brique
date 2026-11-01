#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 15:02:28 2026
@author: Arnaud PAJANI - Ethan MAY
Jeu de casse briques | fichier tkinter
A faire : Tout
"""
import math as m
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
        self.Jeu = tk.Canvas(self.ecran, width=960, height=1080, bg="gray10")
        self.Jeu.pack(side="right")
        
        ### canvas des paramètres ###
        self.Data = tk.Canvas(self.ecran, width=960, height=1080, bg="gray20")
        self.Data.pack(side="left")
        
        ### Donnee pour le jeu ###
        self.partie = False # statut de la partie (true pour commencee, false sinon)
        self.gardeBalle = False
        self.pause = False  # permet de mettre en pause la partie ou d'attendre de relancer la balle apres avoir perdu une vie
        self.lBriques = []
        self.Joueur = jo.Joueur(self.Jeu)
        self.Balle = ba.Balle(self.Jeu)
        self.immortel = False
        self.niv = 1 #Niveau de difficulté
        self.niveau = ni.Niveau(self.niv, "classique", self.Jeu) # ID du niveau
        
        ### affichage textuelle ###
        self.vie = 3
        self.label_vie = tk.Label(self.Jeu, text=f'vie : {self.vie}', font= 'ROGFonts-Regular', bg="gray10", fg="white")
        self.label_vie.place(x=10,y=10)
        self.score = 000000
        self.label_score = tk.Label(self.Jeu, text=f'score : {self.score}', font= 'ROGFonts-Regular', bg="gray10", fg="white")
        self.label_score.place(x=820,y=10)
        self.jeu = tk.StringVar(value='Casse Briques')
        self.label_jeu = tk.Label(self.Data, textvariable=self.jeu, font= 'ROGFonts-Regular', bg="gray20", fg="white")
        self.label_jeu.place(x=410,y=100)
        
        ### les boutons ###
        boutonPartie = tk.Button(self.Data, text ='Start Game', font= 'ROGFonts-Regular', fg="green", command = self.jeuCasseBrique)
        boutonPartie.place(x=410,y=965)
        boutonRecommencer = tk.Button(self.Data, text ='Restart', font= 'ROGFonts-Regular', fg="green", command = self.recommencer)
        boutonRecommencer.place(x=429,y=1000)
        buttonQuitte = tk.Button(self.Data, text="Quitter", font= 'ROGFonts-Regular', fg="red", command=self.ecran.destroy)
        buttonQuitte.place(x=430,y=1035)
        
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
            if not self.partie:
                # Demarre le mouvement de la balle pour le casse brique
                self.Balle.reset()
                self.Balle.dep = True
                self.Balle.deplacement()
                
            else:
                self.activePause()
                
        if touche_pressee == 'g' : # jeu nb rebonds
            self.gardeBalle = True
            self.score.set("Rebond = 0")
            self.jeu.set('Garde la balle')
            self.jeuGardeBalle()
            print("Debut du jeu garder la balle")
                
        if touche_pressee == 'i' :
            self.immortel = True
        
        if touche_pressee == 'm' :
            self.immortel = False
        
        if touche_pressee == 'n' :
            self.niveau += 1

    def jeuGardeBalle(self):
        self.Joueur.reset()
        self.Balle.reset()
        if self.rebondRaquette():
            print("score +1")

    # --------------------------------------------------
    # COLLISIONS
    # --------------------------------------------------

    def intersects(self, a, b):
        if a[0] <= b[2] and a[2] >= b[0] and a[1] <= b[3] and a[3] >= b[1] :
            return True
        return False

    def rebondMurs(self):
        x1, y1, x2, y2 = self.Balle.position()

        if x1 <= 0 and self.Balle.dx < 0:
            self.Balle.rebonfHorizontal()
        elif x2 >= 950  and self.Balle.dx > 0:
            self.Balle.rebonfHorizontal()

        if y1 <= 0 and self.Balle.dy < 0:
            self.Balle.rebondVertical()

    def rebondRaquette(self):
        coordBalle = self.Balle.position()
        coordJoueur = self.Joueur.position()
        if self.intersects(coordBalle, coordJoueur) and self.Balle.dy > 0:
            
            # Replace la balle au-dessus de la raquette
            # pour éviter qu'elle reste coincée dedans.
            self.Jeu.move(self.Balle.nom, 0,coordJoueur[1] - coordBalle[3])
            self.Balle.rebondVertical()

    def rebondBriques(self):
        coordBalle = self.Balle.position()
        for briques in self.lBriques:
            for brique in briques:
                if not brique.vivant:
                    continue
    
                coordBrique = brique.position()
    
                if self.intersects(coordBalle, coordBrique):
                    detruit = brique.touche()
    
                    if detruit:
                        self.actuScore()
                        # ici gain d'un bonus si ajouter 
                        
                    else:
                        self.actuScore() # on obtient des points mais la brique reste
    
                    recouvreX = min(coordBalle[2] - coordBrique[0], coordBrique[2] - coordBalle[0])
                    recouvreY = min(coordBalle[3] - coordBrique[1], coordBrique[3] - coordBalle[1])
    
                    if recouvreX < recouvreY:
                        self.Balle.rebonfHorizontal()
                    else:
                        self.Balle.rebondVertical()
                    break # fin du for 

        
    def actuScore(self):
        self.score += 10     
        self.label_score.config(text=f"Score : {self.score}")
        
    def next_level(self):
        self.niveau.numero += 1
        self.niv += 1         
        self.niveau.genererBriques()
    
    def finPartie(self,message):
        self.partie = False
        self.Jeu.delete("end_message")

        self.Jeu.create_rectangle(180, 410, 720, 690,fill="#202038",outline="white",width=2,tags="end_message")

        self.Jeu.create_text(450, 545,text=message,fill="white",font=("Arial", 28, "bold"),tags="end_message")
        
        self.Jeu.create_text(450, 590,text=f'Score : {self.score}',fill="#ffca3a",font=("Arial", 18),tags="end_message")

    
    def viePerdu(self):
        if self.immortel:
            self.Balle.reset()
            self.Joueur.reset()
            return
        if self.vie > 0:
            self.vie -= 1
            self.label_vie.config(text=f"Vies : {self.vie}")
        if self.vie <= 0:
            self.finPartie("GAME OVER")
        else:
            self.Balle.reset()
            self.Joueur.reset()
                
    def activePause(self):
        self.pause = not self.pause

        if self.pause:
            self.Jeu.delete("pause")
            self.Jeu.create_text(350, 300,text="PAUSE",fill="white",font=("Arial", 28, "bold"),tags="pause")
        else:
            self.Jeu.delete("pause")
                
    # --------------------------------------------------
    # BOUCLE PRINCIPALE
    # --------------------------------------------------

    def jeuCasseBrique(self):
        """
        appel -> pas lance la balle (condition press espace)
                 affiche : espace pour commencer et mettre en pause la partie
                 genere les briques sur le terrain
        """
        if not self.partie:
            self.partie = True
            self.lBriques = self.niveau.genererBriques() 
            
        if not self.pause:
            self.Balle.deplacement()

            self.rebondMurs()
            self.rebondRaquette()
            self.rebondBriques()

            _, _, _, basBalle = self.Balle.position()

            if basBalle >= 1060:
                self.viePerdu()
                
            prochainNiv = 0
            for briques in self.lBriques:
                if self.partie and all(not brique.vivant for brique in briques):
                    prochainNiv += 1
            if prochainNiv == self.niv+4:        
                self.next_level()

        self.Jeu.after(10, self.jeuCasseBrique)

    def recommencer(self):
        self.vie = 3
        self.label_vie.config(text=f"Vies : {self.vie}")
        self.score = 0
        self.label_score.config(text=f"Score : {self.score}")
        self.niv = 1
        self.lBriques = []
        self.Jeu.delete(all)
        self.Jeu.update()
        self.jeuCasseBrique()
               
""" A adapter 
    # --------------------------------------------------
    # SAUVEGARDE JSON
    # --------------------------------------------------

    def load_high_score(self):
        try:
            with open(self.HIGH_SCORE_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)
                return max(0, int(data.get("best_score", 0)))
        except (FileNotFoundError, json.JSONDecodeError,
                ValueError, TypeError, OSError):
            return 0

    def save_high_score(self):
        try:
            with open(self.HIGH_SCORE_FILE, "w", encoding="utf-8") as file:
                json.dump(
                    {"best_score": self.best_score},
                    file,
                    indent=4
                )
        except OSError:
            print("Impossible de sauvegarder le meilleur score.")

    def actuScore(self, points):
        self.score += points

        if self.score > self.best_score:
            self.best_score = self.score
            self.save_high_score()

        self.update_hud()
"""
