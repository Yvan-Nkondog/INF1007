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

    

    # TODO Affichez (print) les trois dataframes

   

    # Assemblage
    # TODO Créez des objets de type Capsule, Reservoir et Moteur
    #  à partir des dataframes

    capsule_1 = None
    reservoir_1 = None
    moteur_1 = None

    # TODO Créez deux fusées

        # TODO Créer une fusée à partir des pièces choisies et ajoutez la à la liste fusees
    pass

        # TODO Afficher (print) la fusée

        

    # Comparaison
    # TODO Affichez les corps célestes accessibles par les deux fusées
    list()  # TODO Remplacer list() par le bon appel de fonction
    list()  # TODO Remplacer list() par le bon appel de fonction

    # TODO Créez et affichez le graphique de comparaison des deux fusées en réutilisant la fonction implémentée
    pass



if __name__ == '__main__':
    main()
