#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Usage:
    lanceur.py (log | lin | quad | pal) [options]

Options:
    -n --nbiter=<1000>   Itérations effectué par le recuit [default: 1000]
    -m --max=<10>        Taille du dernier entier accessible [default: 10]
    -t --temp=<1>     Température initiale [default: 1]
    -h --help            Affiche ce message d'aide
"""

from docopt import docopt
from src.recuit import recuit
from src.glouton import glouton
from src.temperatures import temp_log, temp_lin, temp_quad, temp_palier


def main(nb_iter, entier_max, t_ini, schema_temp):
    """Entrée du script."""
    print(f"Entiers de 1 à {entier_max}")
    print(f"Constante de température : {t_ini}")
    print(f"Schéma de température : {schema_temp.__name__}")
    print(f"Nombre d'itérations : {nb_iter}\n")
    temperature = schema_temp(nb_iter, t_ini)
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
    TEMPERATURE_INI = float(OPTIONS["--temp"])
    if OPTIONS["lin"]:
        SCHEMA = temp_lin
    elif OPTIONS["log"]:
        SCHEMA = temp_log
    elif OPTIONS["quad"]:
        SCHEMA = temp_quad
    elif OPTIONS["pal"]:
        SCHEMA = temp_palier
    main(NB_ITER, ENTIER_MAX, TEMPERATURE_INI, SCHEMA)
