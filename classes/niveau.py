"""
Created on Wed Sep 23 15:02:28 2026
@author: Arnaud PAJANI - Ethan MAY
Jeu de casse-briques | classe Niveau
A faire : Tout
"""



from briques.brique import Brique

class Niveau():
    def __init__(self, pNumero, pNombreBriqueApparaitre, pTailleX, pTailleY) -> None:
        self.numero = pNumero # sera constante par instance
        self.NombreBriqueApparaitre = pNombreBriqueApparaitre # sera constante par instance
        self.briques = self.apparaitreBriques()
        self.tailleX = pTailleX
        self.tailleY = pTailleY

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

    def obtenirNombreBriqueApparaitre(self):
        return self.NombreBriqueApparaitre

    def apparaitreBriques(self):
        """
            Entrée(s) : -
            Sortie(s) : -
            Algo :
        """
        valRen = []
        instances = [Brique(100*i, 20*i, 5*i, 10*i) for i in range(self.NombreBriqueApparaitre)] # codé en dur 
        valRen = instances
        
        return valRen

    def obtenirBriquesRestantes(self, pListe):
        """
            Entrée(s) : liste des briques et statut (list)
            Sortie(s) : briques restantes (int)
            Algo : 
        """
        liste = pListe.copy()
        valRen = []
        for brique in liste:
            if brique.estVivant():
                valRen.append(brique)

        return valRen

    def obtenirNombreBriquesRestantes(self, pListe):
        """
            Entrée(s) : -
            Sortie(s) : briques restantes (int)
            Algo : 
        """
        return len(pListe)



def test():
    niveau = Niveau(1, 1)
    briques = niveau.obtenirBriquesRestantes(niveau.briques)
    print(briques)
    print(niveau.obtenirNombreBriquesRestantes(briques), "brique restante")
    print("\n\n\n")
    print("Gagné =", niveau.estGagne())
    briques[0].durabilite = 0
    print("Gagné =",niveau.estGagne(), "après modif")

test()