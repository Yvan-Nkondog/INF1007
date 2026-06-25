# -*- coding: utf-8 -*-
# Nom_du_fichier: Reservoir.py
# Creer le      : 
# Creer par     : 
# Version num   : 
# Modifier le   : 

import matplotlib.pyplot as plt
import math
from IPython.display import clear_output
from Molecule import moleculesSeTouche, deplacerMolecule, creerListMolecules
from Molecule import ajusteDirApresCollision, inverseDirMolecule


# Fonction ajoutée pour permeetre la création d'une liste de collision.
# Pour n molécules, la liste de collision est de taille n(n-1) / 2.
def creerListeCollision(nbMolecules):
    listeDeCollision = []
    for i in range(nbMolecules):
        for j in range(i + 1, nbMolecules):
            # La liste de collision est initialisée avec des zéros. En cas de
            # collision une fonction va incrémenter ces valeurs.
            listeDeCollision.append(0)
    return listeDeCollision

# Fonction supplémentaire qui permet de vérifier si un paramètre est de type
# "Reservoir".
def estReservoir(argument):
    return (
        isinstance(argument, dict)
        and set(argument.keys()) == {"h", "l", "posPar", "mG",  "mD", "lCG", "lCD"}
    )


def creerReservoir(hauteur,largeur,posParoi,nbMoleculesG,nbMoleculesD):
    #TODO 3.2.1 Créer le structure de données d'un réservoir
    # Utiliser creerListMolecules (voir 3.1.5)
    mG = creerListMolecules(hauteur, 0, posParoi, nbMoleculesG)
    mD = creerListMolecules(hauteur, posParoi, largeur, nbMoleculesD)

    # Générer des listes de collision vides. Dans chaque liste, chaque
    # molécule est appariée une fois avec chaque molécule de la liste.
    lCG = creerListeCollision(nbMoleculesG)
    lCD = creerListeCollision(nbMoleculesD)
    
    return {
        "h": hauteur,
        "l": largeur,
        "posPar": posParoi,
        "mG": mG,
        "mD": mD,
        "lCG": lCG,
        "lCD": lCD
    }


# Fonction ajoutée afin d'éviter la duplication du code
# dans la fonction "colision(reservoir)".
def traiterCollisions(molecules, listeCollision):
    k = 0

    for i in range(len(molecules)):
        for j in range(i + 1, len(molecules)):

            if moleculesSeTouche(molecules[i], molecules[j]):
                ajusteDirApresCollision(
                    molecules[i],
                    molecules[j]
                )
                # Incrémenter la valeur de la liste des collision de zéro à 1, 
                # lorsqu'il y a collision.
                listeCollision[k] = 1

            k += 1
  
def colision(reservoir):
    #TODO 3.2.2 Vérifier si il y a des collisions entre des molécules dans un réservoir
    # Pour chaque molécule vérifier si elles est en collision avec une autre molécule du réservoir
    if not estReservoir(reservoir):
        raise TypeError("Le paramètre doit être de type 'Reservoir'.")
    
    # Remettre les listes de collision à 0 (utile puisque la fonction est appelée plusieurs fois).
    reservoir["lCG"] = [0] * len(reservoir["lCG"])
    reservoir["lCD"] = [0] * len(reservoir["lCD"])

    traiterCollisions(
        reservoir["mG"],
        reservoir["lCG"]
    )

    traiterCollisions(
        reservoir["mD"],
        reservoir["lCD"]
    )

    return reservoir


def inverseDirMolecules(reservoir):
    #TODO 3.2.3 Ajuster la direction des molécules qui touchent aux parois dans chaque réservoir
    # Faire appel à inverseDirMolecule(mol, paroiG, paroiD, hauteur) (3.2.3)
    if not estReservoir(reservoir):
        raise TypeError("Le paramètre doit être de type 'Reservoir'.")
    
    for molecule in reservoir["mG"]:
        inverseDirMolecule(molecule, 0, reservoir["posPar"], reservoir["h"])

    for molecule in reservoir["mD"]:
        inverseDirMolecule(molecule, reservoir["posPar"], reservoir["l"], reservoir["h"])
        
    return reservoir

# Fonction ajoutée pour éviter la duplication du code dans la fonction getTemperature.
def calculerTemperature(molecules):
    energie = 0

    for molecule in molecules:
        vitesse2 = (
            molecule["dx"]**2
            + molecule["dy"]**2
        )
        # La masse n'a pas été donnée. On suppose qu'elle est égale à une unité.
        energie += 0.5 * vitesse2

    return energie / len(molecules)

def getTemperature(reservoir, cote):
    #TODO 3.2.4 Calcule la température de chaque côté du réservoir.
    # Utiliser la formule dans le Readme
    if not estReservoir(reservoir):
        raise TypeError(
            "Le paramètre doit être de type 'Reservoir'."
        )

    if cote == "Gauche":
        return calculerTemperature(reservoir["mG"])

    elif cote == "Droit":
        return calculerTemperature(reservoir["mD"])
    
    else:
        raise ValueError("Le côté doit être 'Gauche' ou 'Droit'.")

    return temperature


#####################################################
# Donner
#####################################################
def affichage(reservoir):
    txt = "Température côté Gauche: {:.2f}C \t\t\t\t\t Température côté Droit: {:.2f}C".expandtabs()   
    plt.figure(figsize=(20,10))
    plt.plot([reservoir['posPar'], reservoir['posPar']], [0, reservoir['h']], 'k-', linewidth=10) 
    plt.axis([-20, reservoir['l'] + 20, -20, reservoir['h'] + 20])
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.title(txt.format(getTemperature(reservoir, "Gauche"),getTemperature(reservoir, "Droit")),fontsize=23)
    
    for k in [['mG','ro'],['mD','go']]:
        for i in range(len(reservoir[k[0]])):  
            inte = min(max((abs(reservoir[k[0]][i]['dx']) + abs(reservoir[k[0]][i]['dy']))/60,0.2),1)
            plt.clf
            plt.plot(reservoir[k[0]][i]['x'], reservoir[k[0]][i]['y'], k[1], alpha = inte, ms=reservoir[k[0]][i]['rayon'])
            reservoir[k[0]][i] = deplacerMolecule(reservoir[k[0]][i])
    
    # plt.pause(0.01)
    plt.show()
    clear_output() 
    

def deplacerMolecules(reservoir):
    #TODO 3.2.6
    # deplacer_molecule deplace les molecules du reservoir
    # Cette fOnction recoit comme parametre un objet de type reservoir et execute les etapes suivantes:
    if not estReservoir(reservoir):
        raise TypeError("Le paramètre doit être de type 'Reservoir'.")
    # 1) Inverser la direction des molecules du reservoir
    inverseDirMolecules(reservoir)
    # 2) Afficher les molecules
    affichage(reservoir)
    # 3) Determination des colision des molecules
    colision(reservoir)
    
    return reservoir


if __name__ == '__main__':
    hauteur,largeur,posParoi,nbMoleculesG,nbMoleculesD = 2000,2000,1300,100,50
    reservoir = creerReservoir(hauteur,largeur,posParoi,nbMoleculesG,nbMoleculesD)
    for i in range(1000):
        reservoir = deplacerMolecules(reservoir)

    
    

    
    