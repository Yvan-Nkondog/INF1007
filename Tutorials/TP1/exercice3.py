
def decomposer(secondes):
    # Définir, sous forme de constantes, le nombre de secondes, dans une minute,
    # dans une heure, dans une journée, dans une semaine, et dans une année.
    NB_SEC_DANS_MINUTE = 60
    NB_SEC_DANS_HEURE = 60 * NB_SEC_DANS_MINUTE
    NB_SEC_DANS_JOUR = 24 * NB_SEC_DANS_HEURE
    NB_SEC_DANS_SEMAINE = 7 * NB_SEC_DANS_JOUR
    NB_SEC_DANS_ANNEE = 365 * NB_SEC_DANS_JOUR

    # TODO: Assigner à la variable "annees" le nombre d'années
    # On suppose que l'année possède 365 jours
    annees = secondes // NB_SEC_DANS_ANNEE
    reste_secondes = secondes % NB_SEC_DANS_ANNEE

    # TODO: Assigner à la variable "semaines" le nombre de semaines restantes
    semaines = reste_secondes // NB_SEC_DANS_SEMAINE
    reste_secondes %= NB_SEC_DANS_SEMAINE

    # TODO: Assigner à la variable "jours" le nombre de jours restants
    jours = reste_secondes // NB_SEC_DANS_JOUR
    reste_secondes %= NB_SEC_DANS_JOUR

    # TODO: Assigner à la variable "heures" le nombre d'heures restantes
    heures = reste_secondes // NB_SEC_DANS_HEURE
    reste_secondes %= NB_SEC_DANS_HEURE

    # TODO: Assigner à la variable "minute" le nombre de minutes restantes
    minutes = reste_secondes // NB_SEC_DANS_MINUTE
    reste_secondes %= NB_SEC_DANS_MINUTE                 

    # TODO: Assigner à la variable "secondes" le nombre de secondes restantes
    secondes = reste_secondes

    # TODO: Afficher le nombres d'années, semaines, jours, heures, minutes et secondes
    print(annees, semaines, jours, minutes, secondes)

    return annees, semaines, jours, heures, minutes, secondes
