from typing import Tuple

import fusee
from assemblage import creer_capsules, creer_reservoirs, creer_moteurs, corps_celestes_accessibles, comparer_fusee
from constantes import IMPULSION_SPECIFIQUE_MINIMALE, CHEMIN_CAPSULES, CHEMIN_RESERVOIRS, CHEMIN_MOTEURS
from fichiers_pieces import charger_capsules_df, charger_reservoirs_df, charger_moteurs_df, filtrer_moteurs
from fusee import Fusee


def main() -> Tuple[Fusee, Fusee]:
    # Pièces
    # Chargement des pièces
    capsules_df = charger_capsules_df(CHEMIN_CAPSULES)
    reservoirs_df = charger_reservoirs_df(CHEMIN_RESERVOIRS)
    moteurs_df = charger_moteurs_df(CHEMIN_MOTEURS)

    # TODO Filtrez les moteurs avec une impulsion spécifique plus
    #  petite que IMPULSION_SPECIFIQUE_MINIMALE
    moteurs_df = moteurs_df[moteurs_df["impulsion specifique"] >= IMPULSION_SPECIFIQUE_MINIMALE]
    
    # TODO Affichez (print) les trois dataframes
    print(capsules_df, end='\n\n')
    print(moteurs_df, end='\n\n')
    print(reservoirs_df, end='\n\n')
   
    # Assemblage
    # TODO Créez des objets de type Capsule, Reservoir et Moteur
    #  à partir des dataframes

    # Creation des capsules
    capsules = creer_capsules(capsules_df)
    reservoirs = creer_reservoirs(reservoirs_df)
    moteurs = creer_moteurs(moteurs_df)

    # TODO Créez deux fusées
    # TODO Créer une fusée à partir des pièces choisies et ajoutez la à la liste fusees
    noms_fusees = ["Orbite Mars", "Vers le soleil"]
    liste_fusee = []
    liste_fusee.append(Fusee(noms_fusees[0], capsules[2], reservoirs[2], moteurs[0]))
    liste_fusee.append(Fusee(noms_fusees[1], capsules[2], reservoirs[2], moteurs[1]))

    # TODO Afficher (print) la fusée
    print(liste_fusee[0], end='\n\n')

    # Comparaison
    # TODO Affichez les corps célestes accessibles par les deux fusées
    for fusee in liste_fusee:
        print(corps_celestes_accessibles(fusee))  # TODO Remplacer list() par le bon appel de fonction
    
    # Ligne vide ajoutée volontairement pour améliorer l'affichage dans la console.
    print('\n')

    # TODO Créez et affichez le graphique de comparaison des deux fusées en réutilisant la fonction implémentée
    comparer_fusee(liste_fusee[0], liste_fusee[1])

    # Retourner les deux fusées créées dans un tuple.
    return liste_fusee[0], liste_fusee[1]


if __name__ == '__main__':
    main()
