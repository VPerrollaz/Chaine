#! /usr/bin/env python

# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright https://github.com/VPerrollaz
#
# Distributed under terms of the %LICENSE% license.

"""
Test concernant recuit.py
"""
from src.recuit import auxiliaire
from math import isclose


def test_auxiliaire():
    """Test de la forme."""
    for nbr in range(1, 11):
        assert isclose(auxiliaire(nbr), (nbr * auxiliaire(1 / nbr)))
