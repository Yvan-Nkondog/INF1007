import math


def calculerPosition(positionInitiale, vitesseInitiale, duree, vitesseFinale):
    # TODO faites les calculs intermediaires, vous pouvez initialiser des variables locales.
    a = 0
    # Harmonisation des unités (en mètre, seconde, m/s, m/s^2)
    CONSTANTE_CONVERSION_EN_METRE_PAR_SECONDE = 1000 / 3600
    vitesse_initiale_metre_par_seconde = vitesseInitiale * CONSTANTE_CONVERSION_EN_METRE_PAR_SECONDE
    vitesse_finale_metre_par_seconde = vitesseFinale * CONSTANTE_CONVERSION_EN_METRE_PAR_SECONDE

    # Calculer l'accération à partir de la formule fournie (en m / s^2)
    acceleration = (vitesse_finale_metre_par_seconde - vitesse_initiale_metre_par_seconde) / duree

    # Calculer la variation de position, à partir de la formule fournie.
    delta_position = (vitesse_initiale_metre_par_seconde * duree) + (0.5 * acceleration * (duree ** 2))
    
    # TODO calculer la position finale, assigner la valeur à la variable "positionFinale"
    positionFinale = positionInitiale + delta_position

    return positionFinale
