from typing import List

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from constantes import DELTA_V_MINIMUM_PAR_CORPS_CELESTE, CHEMIN_CAPSULES, CHEMIN_MOTEURS, CHEMIN_RESERVOIRS
from fichiers_pieces import charger_capsules_df, charger_moteurs_df, charger_reservoirs_df
from fusee import Fusee, Capsule, Reservoir, Moteur


def creer_capsules(capsules_df: pd.DataFrame) -> List[Capsule]:
    # TODO Transformez le dataframe des capsules en liste d'objets de type Capsule
    liste_capsules = []
    for rangee in capsules_df.values:
        capsule = Capsule(
                nom=rangee[0],
                hauteur=rangee[1],
                masse=rangee[2],
                prix=rangee[3],
                places=rangee[4]
                )
        liste_capsules.append(capsule)

    return liste_capsules


def creer_moteurs(moteurs_df: pd.DataFrame) -> List[Moteur]:
    # TODO Transformez le dataframe des moteurs en liste d'objets de type Moteur
    liste_moteurs = []
    for rangee in moteurs_df.values:
        moteur = Moteur(
            nom=rangee[0],
            hauteur=rangee[1],
            masse=rangee[2],
            prix=rangee[3],
            impulsion_specifique=rangee[4]
        )
        liste_moteurs.append(moteur)

    return liste_moteurs
   


def creer_reservoirs(reservoirs_df: pd.DataFrame) -> List[Reservoir]:
    # TODO Transformez le dataframe des reservoir en liste d'objets de type Reservoir
    liste_reservoirs = []
    for rangee in reservoirs_df.values:
        reservoir = Reservoir(
            nom=rangee[0],
            hauteur=rangee[1],
            masse_vide=rangee[2],
            prix=rangee[3],
            capacite=rangee[4]
        )
        liste_reservoirs.append(reservoir)

    return liste_reservoirs


def corps_celestes_accessibles(fusee: Fusee) -> List[str]:
    # TODO Retournez la liste des corps célestes accessibles par la fusée.
    # Utiliser DELTA_V_MINIMUM_PAR_CORPS_CELESTE
    return [corps_celeste for corps_celeste in DELTA_V_MINIMUM_PAR_CORPS_CELESTE 
            if fusee.calculer_deltav() > DELTA_V_MINIMUM_PAR_CORPS_CELESTE[corps_celeste]]



def comparer_fusee(fusee_1: Fusee, fusee_2: Fusee) -> None:
    # TODO Générez un dataframe avec trois colonnes; fusée, résultats des différents ratios et type_ratio
    # Calcul des rapports pour la fusée 1

    # Créer une liste de dictionnaires de valeurs.
    types_ratios = ['DeltaV / Masse', 'DeltaV / Coût', 'Hauteur / Masse']
    liste_donnees = []
    for fusee in (fusee_1, fusee_2):
        dict_donnees = {}
        valeurs_ratios = []
        # Multiplication par len(types_ratios) afin que toutes les listes
        # aient la même taille.
        dict_donnees['Fusée'] = [fusee.nom] * len(types_ratios)
        valeurs_ratios.append(fusee.calculer_deltav() / fusee.masse)
        valeurs_ratios.append(fusee.calculer_deltav() / fusee.prix)
        valeurs_ratios.append(fusee.hauteur / fusee.masse)
        
        
        dict_donnees['Ratios'] = valeurs_ratios
        dict_donnees['Type ratio'] = types_ratios
        liste_donnees.append(dict_donnees)

    # Génerer la dataframe à partir de la liste de dictionnaires.
    liste_df = []
    for dict_donnee in liste_donnees:
        liste_df.append(pd.DataFrame(dict_donnee))
    
    df = pd.concat(liste_df, ignore_index=True)
    print(df)

    # TODO créer un grouped barplot comparant les fusées passées en paramètre en fonction des trois métriques suivantes:
    #  * DeltaV / Masse
    #  * DeltaV / Coût
    #  * Hauteur / Masse
    
    # Références pour la figure tracée.
    # https://www.bing.com/search?q=Grouped+bar+plot+with+the+following+dataframe%2C+python%2C+seaborn%2C+pandas+Fusee+Ratios+Type+ratio+0+Romano+Fafard+0.021919+DeltaV+%2F+Masse+1+Romano+Fafard+0.145366+DeltaV+%2F+Co%C3%BBt+2+Romano+Fafard+0.000110+Hauteur+%2F+Masse+3+Romano+Fafard+Lite+0.001142+DeltaV+%2F+Masse+4+Romano+Fafard+Lite+0.000460+DeltaV+%2F+Co%C3%BBt+5+Romano+Fafard+Lite+0.000872+Hauteur+%2F+Masse&cvid=4fbe6d8f586f463da7fa18ad7a16c68d&gs_lcrp=EgRlZGdlKgYIABBFGDkyBggAEEUYOdIBCDEyMDBqMGo3qAIAsAIA&FORM=ANNTA1&PC=DCTS
    # https://www.bing.com/search?q=sns+group+barplots.+Put+legend+out+of+figure&cvid=a729abd0ed8e4d158821f2a342f55f48&gs_lcrp=EgRlZGdlKgYIABBFGDkyBggAEEUYOdIBCTE1MjYxajBqN6gCALACAA&FORM=ANNTA1&PC=DCTS

    # Ajuster le thème de 'Seaborn' pour obtenir une meilleure représentation.
    sns.set_theme(style="whitegrid")

    # Créer le diagramme à barres groupées (grouped bar plot).
    plt.figure(figsize=(8, 5.5))
    ax = sns.barplot(
        # Définir la couleur des barres.        
        palette="Set1",
        # Passer la 'dataframe' en paramètre.   
        data=df,
        # Catégorie sur l'axe des abscisses (Fusée).
        x=df.columns[0],
        # Valeurs sur l'axe des ordonnées (Ratios)    
        y=df.columns[1], 
        # Nombre de barres par groupe (dépend de 'Type ratio')          
        hue=df.columns[2],        
    )

    # Nommer les axes et ajouter un titre au graphique.
    ax.set_xlabel(df.columns[0], fontsize=14) # df.columns[0] = Fusée
    ax.set_ylabel(df.columns[1], fontsize=14) # df.columns[1] = Ratios
    ax.set_title(f"Comparaison des ratios pour les fusées"
                 f"\n{fusee_1.nom} et {fusee_2.nom}", fontsize=16)
    
    # Ajouter une légende au graphique, à l'extérieur de la figure principale.
    plt.legend(
        # Placer la légende hors du cadre de la figure principale.
        # Valeur1 : sort la légende de la figure principale.
        # Valaur2 : Ajuste la position de la légende verticalement.
        bbox_to_anchor=(1.39, 0.60),
        title=df.columns[2],    # df.columns[2] = 'Type ratio'
        )

    plt.tight_layout()
    
    # Afficher la figure
    plt.show()


if __name__ == '__main__':
    # creer_capsules
    capsules_df = charger_capsules_df(CHEMIN_CAPSULES)
    capsules = creer_capsules(capsules_df)
    for capsule in capsules:
        print(capsule)
    print()

    # creer_moteurs
    moteurs_df = charger_moteurs_df(CHEMIN_MOTEURS)
    moteurs = creer_moteurs(moteurs_df)
    for moteur in moteurs:
        print(moteur)
    print()

    # creer_reservoirs
    reservoirs_df = charger_reservoirs_df(CHEMIN_RESERVOIRS)
    reservoirs = creer_reservoirs(reservoirs_df)
    for reservoir in reservoirs:
        print(reservoir)
    print()

    # corps_celestes_accessibles
    capsule = Capsule("PasDBonSens", 1.5, 840.0, 600.0, 1)
    reservoir_1 = Reservoir("Piscine", 25.0, 9000.0, 13000.00, 6480.0)
    moteur = Moteur("La Puissance", 12.0, 15000.0, 39000.00, 295)
    fusee_1 = Fusee("Romano Fafard", capsule, reservoir_1, moteur)

    deltaV = fusee_1.calculer_deltav()
    corps_celestes = corps_celestes_accessibles(fusee_1)
    print(f"La fusée {fusee_1.nom} peut aller, avec {deltaV:.2f} de deltaV, jusqu'à: {corps_celestes}")
    print()

    # comparer_fusee
    reservoir_2 = Reservoir("Pichet", 0.4, 0.5, 20, 2)
    fusee_2 = Fusee("Romano Fafard Lite", capsule, reservoir_2, moteur)
    comparer_fusee(fusee_1, fusee_2)
