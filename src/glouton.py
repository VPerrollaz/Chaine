#! /usr/bin/env python

# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright https://github.com/VPerrollaz
#
# Distributed under terms of the %LICENSE% license.

"""
Fonction utilisant un graphe et implémentant l'algorithme glouton pour générer une chaine.
"""


def glouton(gra):
    """Récupère un Graphe, renvoit la chaine générée."""
    chaine = list()
    visites = set()
    premier = gra.demarrage[0]
    chaine.append(premier)
    visites.add(premier)
    while True:
        courant = chaine[-1]
        for voisin in gra.voisins[courant]:
            if voisin not in visites:
                chaine.append(voisin)
                visites.add(voisin)
                break
        else:
            return chaine
