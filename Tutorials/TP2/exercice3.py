def compute_pi(p):
    # TODO calculer la valeur de pi d'après la formule donnée dans l'énoncé
    n_serie = 0
    estimation_pi = 0
    signe = 1
    while True:
        terme_iteration = 4 * signe / ((2 * n_serie) + 1)
        estimation_pi += terme_iteration
       
        if abs(terme_iteration) <= (10** (-p)):
            break

        n_serie += 1
        signe *= -1

    # Le nombre d'itération retourné correspond à (n_serie + 1),
    # car la serié va de zéro à infini, et non de "un" à infini.
    return estimation_pi, n_serie + 1


if __name__ == '__main__':
    # Calcul de π (pi)
    pi = 3.141592653589793
    p = 5
    computed_pi , nb_iter = compute_pi(p)
    print("La valeur réel de pi est : {}".format(pi))
    print("La valeur approché de pi à 10e-{} est : {}".format(p, computed_pi))
    print("Résultat obtenu après {} itérations".format(nb_iter))
    