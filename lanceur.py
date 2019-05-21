#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Usage:
    lanceur.py [--max=<max>] [--nbiter=<nbiter>]

Options:
    -n --nbiter=<1000>   Nombre d'itération effectué par le recuit [default: 1000]
    -m --max=<100>       Taille du dernier entier accessible [default: 10]
    -h --help            Affiche ce message d'aide
"""
from docopt import docopt
from src.recuit import temp_log, recuit
from src.glouton import glouton


def main(nb_iter, entier_max):
    """Entrée du script."""
    print(f"Entier de 1 à {entier_max}")
    print(f"Nombre d'itérations : {nb_iter}\n")
    temperature = temp_log(nb_iter, float(entier_max))
    resultat, meilleure, t_finale = recuit(entier_max, temperature)
    print(f"Meilleure chaine : {meilleure}")
    print(f"Longueur : {len(meilleure)}\n")
    print(f"Chaine finale : {glouton(resultat)}")
    print(f"Longueur : {len(glouton(resultat))}\n")
    print(f"Température finale : {t_finale}")


if __name__ == "__main__":
    OPTIONS = docopt(__doc__)
    NB_ITER = int(OPTIONS["--nbiter"])
    ENTIER_MAX = int(OPTIONS["--max"])
    main(NB_ITER, ENTIER_MAX)
