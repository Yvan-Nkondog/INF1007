
# Initialisation des variables

capital = 8000
nb_jours = 72
taux_annuel = 0.065

# Calcul du taux périodique
taux_periodique = taux_annuel / 365   # taux journalier

# Calcul des intérêts
interets = nb_jours * taux_periodique * capital


# Calcul de la valeur acquise
valeur_acquise = capital + interets

# Affichage des intérêts et de la valeur acquise
print("Les intérêts gagnés après 72 jours sont: ", interets, sep='\n')
print("La valeur acquise après 72 jours est: ", valeur_acquise, sep='\n')
