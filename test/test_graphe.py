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

from src.graphe import Genre, Graphe, Mouvement, echange


def test_echange():
    """Vérification simple."""
    liste = [1, 2]
    echange(liste, 1, 2)
    assert liste == [2, 1]


def test_mouvement_demarrage():
    """Test d'un mouvement sur le démarrage."""
    mouv = Mouvement((1, 2))
    assert repr(mouv) == "Mouvement((1, 2))"
    assert mouv.genre is Genre.Demarrage


def test_mouvement_voisinage():
    """Test d'un mouvement sur le voisinage."""
    mouv = Mouvement((1, 2, 3))
    assert repr(mouv) == "Mouvement((1, 2, 3))"
    assert mouv.genre is Genre.Voisinage


def test_graphe_adhoc():
    """Via le constructeur basique."""
    graphe = Graphe(demarrage=[1, 2, 3], voisinage={1: [2, 3], 2: [1], 3: [1]})
    assert isinstance(graphe, Graphe)


def test_initialisation_simplissime():
    """Vérification sur le graphe le plus simple."""
    gra = Graphe.default(2)
    assert gra.demarrage == [1, 2]
    assert (gra.voisinage[1] == [2]) and (gra.voisinage[2] == [1])


def test_initialisation_moins_simple():
    """Cas plus complexe."""
    gra = Graphe.default(10)
    assert gra.demarrage == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert gra.voisinage[1] == list(range(2, 11))
    assert gra.voisinage[2] == [1, 4, 6, 8, 10]
    assert gra.voisinage[3] == [1, 6, 9]
    assert gra.voisinage[4] == [1, 2, 8]
    assert gra.voisinage[5] == [1, 10]
    assert gra.voisinage[6] == [1, 2, 3]
    assert gra.voisinage[7] == [1]
    assert gra.voisinage[8] == [1, 2, 4]
    assert gra.voisinage[9] == [1, 3]
    assert gra.voisinage[10] == [1, 2, 5]
