# -*- coding: utf-8 -*-
# Nom_du_fichier: Reservoir.py
# Creer le      : 
# Creer par     : 
# Version num   : 
# Modifier le   : 

import matplotlib.pyplot as plt
from IPython.display import clear_output
from Molecule import moleculesSeTouche, deplacerMolecule, creerListMolecules
from Molecule import ajusteDirApresCollision, inverseDirMolecule


def creerReservoir(hauteur,largeur,posParoi,nbMoleculesG,nbMoleculesD):
    #TODO 3.2.1 Créer le structure de données d'un réservoir
    # Utiliser creerListMolecules (voir 3.1.5)
    
    return ...

  
        
def colision(reservoir):
    #TODO 3.2.2 Vérifier si il y a des collisions entre des molécules dans un réservoir
    # Pour chaque molécule vérifier si elles est en collision avec une autre molécule du réservoir


    return ...


def inverseDirMolecules(reservoir):
    #TODO 3.2.3 Ajuster la direction des molécules qui touchent aux parois dans chaque réservoir
    # Faire appel à inverseDirMolecule(mol, paroiG, paroiD, hauteur) (3.2.3)

    return ...

def getTemperature(reservoir, cote):
    #TODO 3.2.4 Calcule la température de chaque côté du réservoir.
    # Utiliser la formule dans le Readme

    return ...


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
            plt.plot(reservoir[k[0]][i]['x'], reservoir[k[0]][i]['y'], k[1], alpha = inte, ms=reservoir[k[0]][i]['rayon'])
            reservoir[k[0]][i] = deplacerMolecule(reservoir[k[0]][i])
    
    plt.pause(0.01)
    clear_output() 
    

def deplacerMolecules(reservoir):
    #TODO 3.2.6
    # deplacer_molecule deplace les molecules du reservoir
    # Cette function recoit comme parametre un objet de type reservoire est execute les etapes suivantes:
    # 1) Inverser la direction des molecules du reservoir

    # 2) Afficher les molecules

    # 3) Determination des colision des molecules

    return ...

if __name__ == '__main__':
    hauteur,largeur,posParoi,nbMoleculesG,nbMoleculesD = 2000,2000,1300,100,50
    reservoir = creerReservoir(hauteur,largeur,posParoi,nbMoleculesG,nbMoleculesD)
    for i in range(1000):
        reservoir = deplacerMolecules(reservoir)

    
    

    
    