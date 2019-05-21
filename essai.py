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
from src.recuit import temp_log, recuit
from src.glouton import glouton


def main():
    """Entrée du script."""
    temperature = temp_log(100, 10.0)
    resultat = recuit(10, temperature)
    print(resultat)
    print(glouton(resultat))


if __name__ == "__main__":
    main()
