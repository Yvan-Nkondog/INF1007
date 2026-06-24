# -*- coding: utf-8 -*-
# Nom_du_fichier: Molecule.py
# Creer le      : 
# Creer par     : 
# Version num   : 
# Modifier le   : 

from random import randint, randrange
import math


def creerMolecule(x, y, dx, dy, rayon):
    #TODO 3.1.1 Créer le dictionnaire pour représenter une molécule
    return {"x": x, "y": y, "dx": dx, "dy": dy, "rayon": rayon}


# Fonction supplémentaire qui permet de vérifier si un paramètre est de type
# molécule.
def estMolecule(argument):
    return (
        isinstance(argument, dict)
        and set(argument.keys()) == {"x", "y", "dx", "dy", "rayon"}
    )


def moleculesSeTouche(mol_1, mol_2):
    #TODO 3.1.2 Implémenter la formule pour vérifier si deux molécules se touche
    # Renvoi vrai si les molécules se touchent, faux si non
    if not (estMolecule(mol_1) and estMolecule(mol_2)):
        raise TypeError("Le paramètre doit être de type 'molécule'.")
    
    return math.sqrt(((mol_2["x"] - mol_1["x"])**2) + 
                         ((mol_2["y"] - mol_1["y"])**2)) < ((mol_1["rayon"]) + (mol_2["rayon"]))


def deplacerMolecule(mol):
    #TODO 3.1.3 Faire le déplacement de la molécule
    if not estMolecule(mol):
        raise TypeError("Le paramètre doit être de type 'molécule'.")
    mol["x"] += mol["dx"]
    mol["y"] += mol["dy"]
    return mol

    
#####################################################
# Donner
#####################################################
def ajusteDirApresCollision(mol_1, mol_2):
    deltaX = mol_2['x'] - mol_1['x']
    dVx = 0

    if (deltaX == 0.0):
        dVy = mol_2['y'] - mol_1['y']
    else:
        r = (mol_2['y'] - mol_1['y']) / deltaX
        dVx = (mol_2['dx'] - mol_1['dx'] + (mol_2['dy'] - mol_1['dy']) * r) / (1 + r * r)
        dVy = r * dVx

    mol_1['dx'] += dVx
    mol_1['dy'] += dVy
    mol_2['dx'] -= dVx
    mol_2['dy'] -= dVy

    return mol_1, mol_2


def creerListMolecules(hauteur,xmin,xmax,nbMolecules):
    #TODO 3.1.5 Remplir la liste de molécule comme déctrit dans le README
    # vous pouvez utiliser rayon = randrange(10,30,2) et randint pour x,y,dx,dy

    list_molecules = []
    for i in range(nbMolecules):
        rayon = randrange(10, 30, 2)
        # La position de la molécule ne peut pas dépasser la paroi sur
        # l'axe x. Il faut par conséquent assurer que le centre de la molécule
        # ne déborde pas une distance (xmin + rayon) ou (xmax - rayon).
        # NB: La position d'une molécule est mésurée à partir de son centre.
        x = randint(xmin + rayon, xmax - rayon)
        y = randint(rayon, hauteur - rayon)
        dx = randint(round(xmin/2), round(xmax/2))
        dy = randint(0, round(hauteur/2))

        # Créer la molécule à partir des données aléatoires et ajouter là
        # à la liste des molécules.
        list_molecules.append(creerMolecule(x, y, dx, dy, rayon))
    return list_molecules


def inverseDirMolecule(mol, paroiG, paroiD, hauteur):
    #TODO 3.1.6 Implémenter la fonction décrite dans le README.
    # InverseDirMolecule inverse la direction de la molécule.
    # Cette fonction reçoit en entrer quatre paramètres:
    # la molécule les parois gauche et droit du chaque côté du réservoir et la hauteur du reservoir.
    # Si la molécule touche une des parois du réservoir un faut la reposition à la limite
    # du réservoir et inverser sa direction en vitesse.

    # Valider que le paramètre "mol" est de type "molecule".
    if not estMolecule(mol):
        raise TypeError("Le paramètre doit être de type 'molécule'.")

    # Si la molécule touche la paroi gauche du réservoir en x
    if ((mol["x"] - mol["rayon"]) <= paroiG):
        # Repositionner la molécule et changer sa direction dx
        mol["x"] = paroiG + mol["rayon"]
        mol["dx"] *= -1

    # Si la molécule touche la paroi droite du réservoir en x
    if ((mol["x"] + mol["rayon"]) >= paroiD):
        # Repositionner la molécule et changer sa direction dx
        mol["x"] = paroiD - mol["rayon"]
        mol["dx"] *= -1

    # Si la molécule touche la paroi gauche du réservoir en y
    if ((mol["y"] - mol["rayon"]) <= 0):
        # Repositionner la molécule et changer sa direction dy
        mol["y"] = mol["rayon"]
        mol["dy"] *= -1

    # Si la molécule touche la paroi droite du réservoir en y
    if ((mol["y"] - mol["rayon"]) >= hauteur):
        # Repositionner la molécule et changer sa direction dy
        mol["y"] = hauteur - mol["rayon"]
        mol["dy"] *= -1

    # Retourner la molécule avec la direction inversée.
    return mol


if __name__ == '__main__':
    # Test creerMolecule
    x, y, dx, dy, rayon = 5, 2, -3, 4, 5
    mol = creerMolecule(x, y, dx, dy, rayon)
    text = "La position de la molecule est ({},{}), sa vitesse est ({},{}) "
    text += "et son rayon est {}"
    
    print(text.format(mol['x'],mol['y'],mol['dx'],mol['dy'],mol['rayon']))
    
    # Test moleculesSeTouche
    
    mol_1  = creerMolecule(x, y, dx, dy, rayon)
    mol_2  = mol_1
    result = moleculesSeTouche(mol_1,mol_2)
    
    print("Est ce que les deux molecules se touche: {}".format(result))
       
    mol_2  = creerMolecule(x, y+rayon, dx, dy, rayon)
    result = moleculesSeTouche(mol_1,mol_2)
    
    print("Est ce que les deux molecules se touche: {}".format(result))
    
    mol_2  = creerMolecule(x+rayon, y+rayon, dx, dy, rayon)
    result = moleculesSeTouche(mol_1,mol_2)
    
    print("Est ce que les deux molecules se touche: {}".format(result))
    
    mol_2  = creerMolecule(x+rayon, y+rayon, dx, dy, rayon/4)
    result = moleculesSeTouche(mol_1,mol_2)
    
    print("Est ce que les deux molecules se touche: {}".format(result))
    
    mol_2  = creerMolecule(x+rayon, y+2*rayon, dx, dy, rayon)
    result = moleculesSeTouche(mol_1,mol_2)
    
    print("Est ce que les deux molecules se touche: {}".format(result))
    
    # Test deplacerMolecule
    
    old_text = "Avant le deplacement \n\t" + text
    print(old_text.format(mol['x'],mol['y'],mol['dx'],mol['dy'],mol['rayon']))
    
    mol = deplacerMolecule(mol)
    new_text = "Apres le deplacement \n\t" + text
    print(new_text.format(mol['x'],mol['y'],mol['dx'],mol['dy'],mol['rayon']))
