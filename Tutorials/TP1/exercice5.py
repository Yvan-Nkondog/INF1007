def pointDeRencontre(v1, v2, distance):
    # TODO faites les calculs intermediaires, vous pouvez initialiser des variables locales.
    # Calculer la proportion de déplacement relativement au véhicule 1
    # (NB : La somme des deux proportions devrait donner une unité).
    fraction_de_position_relative_a_v1 = (v1) / (v1 + v2)
    
    # TODO calculer la position de rencontre, assignez la valeur à la variable "positionRencontre"
    
    positionRencontre = distance * fraction_de_position_relative_a_v1

    return positionRencontre
