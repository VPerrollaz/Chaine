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


def echange(liste, el1, el2):
    """Echange les éléments el1 et el2 dans la liste."""
    ind1 = liste.index(el1)
    ind2 = liste.index(el2)
    liste[ind1] = el2
    liste[ind2] = el1


class Graphe:
    """Classe permettant la paramétrisation d'un algorithme glouton."""

    def __init__(self, N):
        self.nb_max = N
        self.demarrage = list(range(1, N + 1))
        self.voisins = dict()
        for i in range(1, N + 1):
            self.voisins[i] = list()
            for j in range(1, N + 1):
                if i == j:
                    continue
                if (i % j == 0) or (j % i == 0):
                    self.voisins[i].append(j)
        self.hist_d = list()
        self.hist_v = list()

    def __repr__(self):
        return f"Graphe({self.nb_max})"

    def __str__(self):
        return "{}\n{}".format(self.demarrage, self.voisins)

    def mutation(self):
        """Détermine une transition possible et l'ajoute à l'historique."""
        entier1, entier2 = rd.sample(self.demarrage, 2)
        echange(self.demarrage, entier1, entier2)
        self.hist_d.append((entier1, entier2))
        entier = rd.choice(self.demarrage)
        voisin1, voisin2 = rd.sample(self.voisins[entier], 2)
        echange(self.voisins[entier], voisin1, voisin2)
        self.hist_v.append((entier, voisin1, voisin2))
