#! /usr/bin/env python

# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright https://github.com/VPerrollaz
#
# Distributed under terms of the %LICENSE% license.

"""
Test de l'algorithme glouton.
"""
from src.graphe import Graphe
from src.glouton import glouton


def test_glouton_simple():
    """Test de l'algorithme glouton sur le graphe le plus simple."""
    graphe = Graphe(2)
    assert glouton(graphe) == [1, 2]


def test_glouton():
    """Cas moins simple"""
    graphe = Graphe(10)
    assert glouton(graphe) == [1, 2, 4, 8]
