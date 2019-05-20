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


def h(u):
    """Fonction auxiliaire de l'algorithme de recuit."""
    return u / (1 + u)
