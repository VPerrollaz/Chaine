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
