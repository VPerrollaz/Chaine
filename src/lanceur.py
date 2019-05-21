#! /usr/bin/env python

# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright https://github.com/VPerrollaz
#
# Distributed under terms of the %LICENSE% license.

"""
Usage:
    lanceur [options]
Options:
    -h --help               Affiche ce message d'aide
    -n --nbiter=<NB_ITER>   Nombre d'itération effectué par le recuit [default: 1000]
    -m --max=<ENTIER_MAX>   Taille du dernier entier accessible [default: 10]
"""
from docopt import docopt
from src.recuit import temp_log, recuit
from src.glouton import glouton


def main(nb_iter, entier_max):
    """Entrée du script."""
    print("Nombre d'itérations : ", nb_iter)
    temperature = temp_log(nb_iter, float(entier_max))
    resultat, meilleure = recuit(entier_max, temperature)
    print("Meilleure chaine : ", meilleure)
    print("Chaine finale : ", glouton(resultat))


if __name__ == "__main__":
    OPTIONS = docopt(__doc__)
    NB_ITER = int(OPTIONS["--nbiter"])
    ENTIER_MAX = int(OPTIONS["--max"])
    main(NB_ITER, ENTIER_MAX)
