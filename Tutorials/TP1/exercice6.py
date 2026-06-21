import matplotlib.pyplot as plt
import math
import numpy as np


def trouverAngle(nombreComplexe):
    return np.angle(nombreComplexe, deg=True)

def trouverModule(nombreComplexe):
    # TODO: Calculer le module du nombre complexe et l'assigner dans "module"
    module = 0

    return module



def effectuerRotation(nombreComplexe, angle_rotation, trouverModule):

    module = trouverModule(nombreComplexe)
    angle = trouverAngle(nombreComplexe)

    # TODO: Afficher le module et l'angle du nombre complexe (3 decimales de précision)
   
    # TODO: Calculer le nouveau nombre complexe après rotation, assigner le nouveau nombre complexe à la variable 'resultat'

    resultat = 0

    nouveauModule = 0
    nouvelAngle = 0

    # TODO : Afficher le nouveau module et le nouvel angle du nombre complexe après rotation (3 decimales de précision)

    return resultat


def dessiner(number, label):
    if number != None:
        plt.polar([0, math.radians(trouverAngle(number))], [0, trouverModule(number)], marker='o', label=label)

if __name__ == '__main__':
    nombre = complex(input("Veuillez entrer un nombre complexe de votre choix sous la forme a+bj (exemple: 1+2j): "))
    rotation = float(input("Veuillez entrer un angle de rotation (en degres) de votre choix (exemple: 87): "))

    try:
        resultat = effectuerRotation(nombre, rotation, trouverModule)
    except Exception as e:
        print(e)
        resultat = None

    dessiner(nombre, 'Avant rotation')
    dessiner(resultat, 'Après rotation')
    plt.legend()
    plt.show()
