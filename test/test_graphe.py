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

from src.graphe import Graphe, Mouvement, echange


def test_echange():
    """Vérification simple."""
    liste = [1, 2]
    echange(liste, 1, 2)
    assert liste == [2, 1]


def test_instanciation_mouvement():
    """Test instanciation et repr sur le graphe à trois sommets."""
    mouv = Mouvement((1, 2), (1, 2, 3))
    assert repr(mouv) == "Mouvement((1, 2), (1, 2, 3))"


def test_initialisation_simplissime():
    """Vérification sur le graphe le plus simple."""
    gra = Graphe(2)
    assert gra.demarrage == [1, 2]
    assert (gra.voisins[1] == [2]) and (gra.voisins[2] == [1])


def test_initialisation_moins_simple():
    """Cas plus complexe."""
    gra = Graphe(10)
    assert gra.demarrage == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert gra.voisins[1] == list(range(2, 11))
    assert gra.voisins[2] == [1, 4, 6, 8, 10]
    assert gra.voisins[3] == [1, 6, 9]
    assert gra.voisins[4] == [1, 2, 8]
    assert gra.voisins[5] == [1, 10]
    assert gra.voisins[6] == [1, 2, 3]
    assert gra.voisins[7] == [1]
    assert gra.voisins[8] == [1, 2, 4]
    assert gra.voisins[9] == [1, 3]
    assert gra.voisins[10] == [1, 2, 5]
