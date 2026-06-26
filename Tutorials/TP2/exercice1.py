def combine_dic(dic_1, dic_2):
    # TODO Compléter la fonction afin de combiner dic_1 et dic_2
    #      en gardant la valeur max en cas de clef commune
    
    # Vérifier si les deux entrées sont de type 'dict'.
    if not isinstance(dic_1, dict) or not isinstance(dic_2, dict):
        raise TypeError("Les deux entrées doivent être de type 'dict'.")
    
    # Extraire les clés des dictionnaires and un ensemble.
    cles_dictionnaires = set(dic_1) | set(dic_2)

    # Fusionner les deux dictionnaires, après avoir vérifié que la valeur
    # correspondant à chaque clé est numérique.
    dict_resultant = {}
    for cle in cles_dictionnaires:
        valeur_dic_1 = dic_1.get(cle, float('-inf'))
        valeur_dic_2 = dic_2.get(cle, float('-inf'))

        # Vérifier si les entrées comparées sont numériques.
        if not (isinstance(valeur_dic_1, (int, float)) and isinstance(valeur_dic_2, (int, float))):
            raise ValueError(f"La valeur de la cle {cle} doit être numérique.")

        dict_resultant[cle] = max(valeur_dic_1, valeur_dic_2)
    
    return dict_resultant


if __name__ == '__main__':
    # Combinaison de dictionnaire
    dic_1 = {'a': 5, 'b': 2, 'c': 9}
    dic_2 = {'a': 1, 'b': 8, 'd': 17}

    dic_3 = combine_dic(dic_1,dic_2)
    print(dic_3)
    