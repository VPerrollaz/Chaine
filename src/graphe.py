#! /usr/bin/env python

# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright https://github.com/VPerrollaz
#
# Distributed under terms of the %LICENSE% license.

"""
Génération du graphe permettant de coder un algorithme glouton.
"""
import random as rd
from enum import Enum, auto


class Genre(Enum):
    """Enum pour gérer le genre de transition."""

    Demarrage = auto()
    Voisinage = auto()


def echange(liste, el1, el2):
    """Echange les éléments el1 et el2 dans la liste."""
    ind1 = liste.index(el1)
    ind2 = liste.index(el2)
    liste[ind1] = el2
    liste[ind2] = el1


class Mouvement:
    """Classe décrivant un mouvement possible dans un Graphe."""

    def __init__(self, donnees):
        if len(donnees) == 2:
            self.genre = Genre.Demarrage
        else:
            self.genre = Genre.Voisinage
        self.donnees = donnees

    def __repr__(self):
        return "Mouvement({})".format(self.donnees)

    def __str__(self):
        if self.genre is Genre.Demarrage:
            return f"Demarrage: {self.donnees[0]} <-> {self.donnees[1]}"
        return "Voisinage de {} : {} <-> {}".format(*self.donnees)


class Graphe:
    """Classe permettant la paramétrisation d'un algorithme glouton."""

    def __init__(self, demarrage, voisinage):
        self.plus_grand = max(voisinage.keys())
        self.demarrage = demarrage
        self.voisinage = voisinage
        self.dernier = None
        self.admissibles = list()
        for nombre in self.voisinage.keys():
            if len(self.voisinage[nombre]) > 1:
                self.admissibles.append(nombre)

    @classmethod
    def default(cls, nb_sommets):
        """Initialisation par ordre croissant."""
        demarrage = 1
        voisinage = dict()
        for i in range(1, nb_sommets + 1):
            voisinage[i] = list()
            for j in range(1, nb_sommets + 1):
                if i == j:
                    continue
                if (i % j == 0) or (j % i == 0):
                    voisinage[i].append(j)
        return cls(demarrage, voisinage)

    def __repr__(self):
        return f"Graphe({self.demarrage, self.voisinage})"

    def __str__(self):
        return "{}\n{}".format(self.demarrage, self.voisinage)

    def modification(self, mouvement: Mouvement):
        """Modifie le graphe en fonction du mouvement demandé."""
        if mouvement.genre is Genre.Demarrage:
            entier1, entier2 = mouvement.donnees
            if self.demarrage == entier1:
                self.demarrage = entier2
            elif self.demarrage == entier2:
                self.demarrage = entier1
            else:
                raise ValueError("Aucun des deux nombres n'est le démarrage.")
        else:
            entier, voisin1, voisin2 = mouvement.donnees
            echange(self.voisinage[entier], voisin1, voisin2)
        self.dernier = mouvement

    def mutation(self):
        """Détermine une transition possible et l'ajoute à l'historique."""
        if rd.random() > 0.5:
            donnees = (self.demarrage, rd.randint(1, self.plus_grand))
        else:
            entier = rd.choice(self.admissibles)
            voisin1, voisin2 = rd.sample(self.voisinage[entier], 2)
            donnees = (entier, voisin1, voisin2)
        mouv = Mouvement(donnees)
        self.modification(mouv)

    def inversion(self):
        """Annule le dernier mouvement et l'enlève de l'historique."""
        self.modification(self.dernier)
        self.dernier = None
