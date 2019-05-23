#! /usr/bin/env python

# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright https://github.com/VPerrollaz
#
# Distributed under terms of the %LICENSE% license.

"""
Schémas de température.
"""
from math import log, exp


def temp_log(nb_iterations, t_ini):
    """Schéma de température logarithmique."""
    for i in range(2, nb_iterations + 2):
        yield t_ini / log(i)


def temp_lin(nb_iterations, t_ini):
    """Schéma de descente linéaire."""
    for i in range(nb_iterations):
        yield 0.1 + t_ini * (1.0 - i / nb_iterations)


def temp_quad(nb_iterations, t_ini):
    """Schéma de température quadratique."""
    for i in range(nb_iterations):
        yield 0.1 + t_ini * (1.0 - i / nb_iterations) ** 2


def temp_palier(nb_iterations, t_ini):
    """Schéma de température logarithmique par palier."""
    i = 0
    k = 1
    palier = exp(2)
    while i < nb_iterations:
        i += 1
        if i > palier:
            k += 1
            palier = exp(k + 1)
        yield t_ini / k
