def fizzBuzz(n):

    # TODO imprimer la chaine de caractère appropriée avec la fonction print().
    resultat = ""
    if (n % 3 == 0) and (n % 5 == 0):
        resultat = "fizzbuzz"

    elif n % 3 == 0:
        resultat = "fizz"
    
    elif n % 5 == 0:
        resultat = "buzz"

    else:
        resultat = str(n)

    # TODO imprimer la chaine de caractère appropriée avec la fonction print().
    print(resultat)

    #  Assigner ensuite la valeur à la variable resultat et retourner celle-ci avec le mot-clé return.
    return resultat
