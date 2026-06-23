
# Initialisation des variables

cap_initial = 300000
taux_interet = 0.08
nombre_annees = 20

# Calcul du capital au bout de 20 années
# Cn = Cn-1+(Cn-1 * taux_interet)
# Cn = Cn-1(1 + taux_interet)
# Cn-1 = Cn-2(1 + taux_interet)
# ...
# C2 = c1(1 + taux_interêt) = (Co(1+taux_interet)(1+taux_interet)) = Co * (1+taux_interet) ^ n
# C1 = C0(1 + taux_interet)
# => Cn est aussi égal à Co(1 + taux_interet)^n

capital_n = cap_initial * ((1 + taux_interet)**nombre_annees)


# Affichage du capital au bout de 20 années
print(f"Capital au bout de 20 années: {capital_n}")
