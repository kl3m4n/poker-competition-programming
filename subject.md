# Problématique

Un jeu de cartes de poker contient 52 cartes - chaque carte a une couleur qui est l'un des trèfles, carreaux, cœurs ou piques (indiqués par C, D, H, S dans les données d'entrée).

Chaque carte a également une valeur qui est l'un des 2, 3, 4, 5, 6, 7, 8, 9, 10, valet, dame, roi, as (indiqués par 2, 3, 4, 5, 6, 7, 8, 9, T, J, Q, K, A). 2 étant la plus petite valeur et l'as la plus grande.

Une main de poker consiste en 5 cartes distribuées à partir du jeu de cartes. Les mains de poker sont classées selon l'ordre suivant, du plus bas au plus élevé.

Comparer 2 mains et dire qui gagne ou si égalité

# Informations

High Card: Les mains qui ne rentrent pas dans une catégorie supérieure sont classées en fonction de la valeur de leur carte la plus élevée. Si les cartes les plus élevées ont la même valeur, les mains sont classées en fonction de la carte suivante la plus élevée, et ainsi de suite.

Pair: Deux des 5 cartes dans la main ont la même valeur. Les mains qui contiennent toutes les deux une paire sont classées en fonction de la valeur des cartes formant la paire. Si ces valeurs sont les mêmes, les mains sont classées en fonction des valeurs des cartes ne formant pas la paire, dans l'ordre décroissant.

Deux Paires: La main contient 2 paires différentes. Les mains qui contiennent toutes les deux 2 paires sont classées en fonction de la valeur de leur paire la plus élevée. Les mains ayant la même paire la plus élevée sont classées en fonction de la valeur de leur autre paire. Si ces valeurs sont les mêmes, les mains sont classées en fonction de la valeur de la carte restante.

Brelan: Trois cartes dans la main ont la même valeur. Les mains qui contiennent toutes les deux un brelan sont classées en fonction de la valeur des 3 cartes.

Suite: La main contient 5 cartes avec des valeurs consécutives. Les mains qui contiennent toutes les deux une suite sont classées en fonction de leur carte la plus élevée.

Couleur: La main contient 5 cartes de la même couleur. Les mains qui sont toutes les deux de couleur sont classées en utilisant les règles de la carte la plus élevée.

Full: 3 cartes de même valeur, avec les 2 cartes restantes formant une paire. Classé en fonction de la valeur des 3 cartes.

Carré: 4 cartes avec la même valeur. Classé en fonction de la valeur des 4 cartes.

Quinte flush: 5 cartes de la même couleur avec des valeurs consécutives. Classé en fonction de la carte la plus élevée dans la main.

# Inputs

2H 3D 5S 9C KD 2C 3H 4S 8C AH => *2eme gagne avec carte haute*

2H 4S 4C 2D 4H 2S 8S AS QS 3S => *1 gagne avec full contre 2eme avec couleur*

2H 3D 5S 9C KD 2C 3H 4S 8C KH => *1er gagne avec carte haute*

2H 3D 5S 9C KD 2D 3H 5C 9S KH => *Egalité*
