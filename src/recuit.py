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
from math import exp
import random as rd
from src.graphe import Graphe
from src.glouton import glouton


def recuit(nb_max, temperature):
    """Implémente le recuit pour l'itérateur de température donné"""
    graphe = Graphe.default(nb_max)
    meilleure = list()
    for temp in temperature:
        ch1 = glouton(graphe)
        graphe.mutation()
        ch2 = glouton(graphe)
        if len(ch2) > len(ch1):
            if len(ch2) < len(meilleure):
                meilleure = ch2
        elif rd.random() > exp((len(ch2) - len(ch1)) / temp):
            graphe.inversion()
    return graphe, meilleure, temp
