#! /usr/bin/env python

# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright https://github.com/VPerrollaz
#
# Distributed under terms of the %LICENSE% license.

"""
Script de test pour les entiers de 1 à 10.
"""
import sys
from src.recuit import temp_log, recuit
from src.glouton import glouton


def main(nb_iter):
    """Entrée du script."""
    print("Nombre d'itérations : ", nb_iter)
    temperature = temp_log(nb_iter, 10.0)
    resultat, meilleure = recuit(10, temperature)
    print("Meilleure chaine : ", meilleure)
    print("Chaine finale : ", glouton(resultat))


if __name__ == "__main__":
    try:
        NB_ITER = int(sys.argv[1])
    except IndexError:
        NB_ITER = 100
    main(NB_ITER)
