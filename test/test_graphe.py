#! /usr/bin/env python

# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright https://github.com/VPerrollaz
#
# Distributed under terms of the %LICENSE% license.

"""
Teste du module graphe.
"""

from src.graphe import Graphe


def test_initialisation():
    """Vérification de l'instanciation et de la création du graphe le plus simple."""
    gra = Graphe(2)
    assert gra.demarrage == [1, 2]
    assert (gra.voisins[1] == [2]) and (gra.voisins[2] == [1])
