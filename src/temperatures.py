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
from math import log


def temp_log(nb_iterations, cte):
    """Schéma de température logarithmique."""
    for i in range(2, nb_iterations + 2):
        yield cte / log(i)


def temp_lin(nb_iterations, cte):
    """Schéma de descente linéaire."""
    for i in range(nb_iterations):
        yield cte * (nb_iterations - i)
