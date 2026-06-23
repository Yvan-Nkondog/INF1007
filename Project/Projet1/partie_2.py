
# Initialisation des variables
capital_initial_p_1 = 2600
capital_initial_p_2 = capital_initial_p_1 - 60
                                                 
taux_annuel_p_1 = 0.045
taux_annuel_p_2 = 0.1
nb_jours_p_1 = 100
nb_jours_p_2 = 300

# Calcul du montant du capital avec le premier placement au 100ème jour de l'année
capital_final_p_1 = capital_initial_p_1 + (capital_initial_p_1 * (taux_annuel_p_1 / 365) * nb_jours_p_1)

# Calcul du montant du capital avec le deuxième placement au 300ème jour de l'année
capital_final_p_2 = capital_initial_p_2 + (capital_initial_p_2 * (taux_annuel_p_2 / 365) * nb_jours_p_2)

# /!\ AVEC UNE BOUCLE/!\ Calcul du jour à partir duquel le deuxième placement rapporte plus que le premier

nb_jours = 0
capital_final_v1 = 0
capital_final_v2 = 0

while (capital_final_v2 <= capital_final_v1):
    nb_jours += 1
    capital_final_v1 = capital_initial_p_1 + (capital_initial_p_1 * (taux_annuel_p_1 / 365) * nb_jours)
    capital_final_v2 = capital_initial_p_2 + (capital_initial_p_2 * (taux_annuel_p_2 / 365) * nb_jours)

# Affichage des valeurs calculées
print("Montant du capital avec le premier placement au 100ème jour : ", capital_final_p_1, sep='\n ')
print("Montant du capital avec le deuxième placement au 300ème jour : ", capital_final_p_2, sep='\n ')
print("Jour à partir duquel le deuxième placement rapporte plus que le premier: ", nb_jours, sep='\n ')