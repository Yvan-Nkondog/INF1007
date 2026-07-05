import json

import pandas as pd

from constantes import CHEMIN_CAPSULES, CHEMIN_MOTEURS, CHEMIN_RESERVOIRS, FICHIER_CAPSULE, FICHIERS_RESERVOIRS, \
    FICHIERS_MOTEURS


def charger_capsules_df(chemin_capsules: str) -> pd.DataFrame:
    # TODO Retournez un dataframe des capsules décrites dans le fichier FICHIER_CAPSULE
    #  Il faut aussi renommer les colonnes pour que celles-ci soient plus lisibles
    nom_fichier = chemin_capsules + '/' + FICHIER_CAPSULE
    try:
        df = pd.read_csv(nom_fichier)
    except FileNotFoundError:
        print(f"Erreur: Le fichier '{chemin_capsules}' n'a pas été trouvé.")
    except pd.errors.EmptyDataError:
        print(f"Erreur : Le fichier csv est vide.")
    except pd.errors.ParserError as e:
        print(f"Erreur - 'parsing' du fichier csv : {e}")
    except Exception as e:
        print(f"Erreur inattendue : {e}")
    
    # Renommer les colonnes du dataframe.
    df = df.rename(columns={
        'n': 'nom',
        'h': 'hauteur',
        'm': 'masse',
        'p': 'prix',
        'pl': 'places'
    })
    # Retourner la dataframe avec les colonnes renommées
    return df


def charger_reservoirs_df(chemin_reservoirs: str) -> pd.DataFrame:
    # TODO Retournez un dataframe combiné des réservoirs décrits dans
    #  les fichiers FICHIERS_RESERVOIRS
    noms_fichiers = [] 
    for i in range(len(FICHIERS_RESERVOIRS)):
        noms_fichiers.append(chemin_reservoirs + '/' + FICHIERS_RESERVOIRS[i])

    # Charger les fichiers json, dans une liste de dataframes, en utilisant pandas
    dfs = []    # Liste de dataframes (df)
    for i in range(len(FICHIERS_RESERVOIRS)):
        dfs.append(pd.read_json(noms_fichiers[i]))

    # Fusionner (concatener) les dataframes créés dans le fichier dfs
    df_fusionnes = pd.concat(dfs, ignore_index=True)

    return df_fusionnes


def charger_moteurs_df(chemin_moteurs: str) -> pd.DataFrame:
    # TODO Retournez un dataframe combiné des moteurs décrits dans
    #  les fichiers FICHIERS_MOTEURS

    # Generer les noms des fichiers moteurs.
    noms_fichiers = []
    for i in range(len(FICHIERS_MOTEURS)):
        noms_fichiers.append(chemin_moteurs + '/' + FICHIERS_MOTEURS[i])

    # Créer une liste pour garder les données.
    liste_donnees = []
    for i in range(len(FICHIERS_MOTEURS)):
        dict_donnees = {}
        index_ligne_filtree = 0
        with open(noms_fichiers[i], 'r') as fichier:
            for ligne in fichier:
                ligne = ligne.strip()
                # Ignorer les lignes vides et celles commençant par '#'.
                if not ligne or ligne.startswith('#'):
                    continue
                # Separer le contenu de la ligne  en deux sections : le nom et la valeur.
                donnee = ligne.split(sep='=')
                # La première valeur est de type str, les autres sont des valeurs numériques
                # conservés sous forme de string (str).
                if index_ligne_filtree == 0:
                    dict_donnees[donnee[0]] = donnee[1]
                elif index_ligne_filtree == 4:
                    dict_donnees[donnee[0]] = int(donnee[1])
                else:
                    dict_donnees[donnee[0]] = float(donnee[1])
                index_ligne_filtree += 1
            liste_donnees.append(dict_donnees)

    # Créer la dataframe, à partir de la liste de données et retourner la dataframe.
    return pd.DataFrame(liste_donnees)
                                                    

def filtrer_moteurs(moteurs_df: pd.DataFrame, impulsion_minimum: int) -> pd.DataFrame:
    # TODO Retourner un sous-ensemble filtré d'un df de moteurs
    #  où l'impulsion spécifique est au dessus d'un certain seuil
    colonne = 'impulsion specifique'
    return moteurs_df[moteurs_df[colonne] > impulsion_minimum]


if __name__ == '__main__':
    # charger_capsules_df
    capsules = charger_capsules_df(CHEMIN_CAPSULES)
    print(capsules)
    print()

    # charger_reservoirs_df
    reservoirs = charger_reservoirs_df(CHEMIN_RESERVOIRS)
    print(reservoirs)
    print()

    # charger_moteurs_df
    moteurs = charger_moteurs_df(CHEMIN_MOTEURS)
    print(moteurs)
    print()

    # filtrer_moteurs
    moteurs_filtres = filtrer_moteurs(moteurs, 220)
    print(moteurs_filtres)
