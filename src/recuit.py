#! /usr/bin/env python

# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright https://github.com/VPerrollaz
#
# Distributed under terms of the %LICENSE% license.

"""
Implémentation de l'algorithme de recuit simulé.
"""
from math import exp, log
import random as rd
from src.graphe import Graphe
from src.glouton import glouton


def auxiliaire(nombre: float) -> float:
    """Fonction auxiliaire de l'algorithme de recuit."""
    return nombre / (1 + nombre)


def energie(graphe: Graphe, temp: float) -> float:
    """Calcul de l'énergie d'un graphe pour un niveau de température donné."""
    return exp(len(glouton(graphe)) / temp)


def recuit(nb_max, temperature, debug=False):
    """Implémente le recuit pour l'itérateur de température donné"""
    graphe = Graphe.default(nb_max)
    for temp in temperature:
        en1 = energie(graphe, temp)
        graphe.mutation()
        en2 = energie(graphe, temp)
        if rd.random() > auxiliaire(en2 / en1):
            graphe.inversion()
        elif debug:
            print(len(glouton(graphe)), end=", ")
    return graphe


def temp_log(nb_iterations, cte=1.0):
    """Schéma de température logarithmique."""
    for i in range(2, nb_iterations + 2):
        yield cte / log(i)
