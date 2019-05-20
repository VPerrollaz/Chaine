# Chaine d'entier la plus longue

## Description du problème

On considère un nombre entier positif N. On cherche à déterminer la chaine de nombres entiers uniques compris entre 1 et N telle que chaque nombre est soit un diviseur soit un multiple du précédent.

## Description de la méthode

On va coder un algorithme glouton en ordonnant les nombres aux départs et les arrêtes connectant les nombres.
Dans un deuxième temps on va utiliser un algorithme de recuit simulé pour déterminer l'algorithme générant la chaine la plus longue.
Pour les transitions du recuit on va implémenter deux choix
- on tirera au hasard deux états initiaux qu'on permute et un sommet puis deux voisins qu'on permute
- on tirera au harad deux états initiaux adjacents qu'on permute puis un sommet et deux voisins adjacents qu'on permute

Dans les deux cas les probabilité de passer de x à y et de y à x sont égales ce qui simplifie la loi de transition.
