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
from src.graphe import Graphe
from src.glouton import glouton


def auxiliaire(nombre: float) -> float:
    """Fonction auxiliaire de l'algorithme de recuit."""
    return nombre / (1 + nombre)


def energie(graphe: Graphe, temp: float) -> float:
    """Calcul de l'énergie d'un graphe pour un niveau de température donné."""
    return exp(-len(glouton(graphe)) / temp)
