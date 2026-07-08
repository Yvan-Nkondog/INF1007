from animal import calcul_meilleur_animal
from elements_tiktok import FILTRE_FESTIF, MUSIQUE_SEPTEMBER, MUSIQUE_BEZOS_I, FILTRE_ETOILES, MUSIQUE_CHRISTMAS, \
    FILTRE_RALENTI
from mammifere import Chat, LongueurPoils
from oiseau import Cockatiel
from reptile import Serpent
from accessoire import Accessoire, TypeAccessoire
from tiktok import TikTok, CompteTikTok


def main() -> CompteTikTok:
    compte = None
    # TODO : Creer un objet Chat qui s'appelle Wako, avec 4 pattes à poils courts roux
    chat_wako = Chat("Wako", LongueurPoils.COURTS, "roux")

    # TODO : Afficher Wako
    print(chat_wako)

    # TODO : Creer un objet Serpent qui s'appelle Bob, qui est diurne et qui n'est pas venimeux
    bob = Serpent("Bob", est_nocture=False, est_venimeux=True)

    # TODO : Afficher Bob
    print(bob)

    # TODO : Creer un objet Cockatiel qui s'appelle Cookie avec 2 pattes
    cookie = Cockatiel("Cookie", 2)

    # TODO : Afficher cookie
    print(cookie)

    # TODO : Creer un objet Accessoire de type chapeau avec un niveau de mignonnerie de 4
    chapeau = Accessoire("Chapeau", 4, TypeAccessoire.CHAPEAU)

    # TODO : Creer un objet Accessoire de type chaussures avec un niveau de mignonnerie de 6
    chaussures = Accessoire("Chaussures", 6, TypeAccessoire.CHAUSSURES)

    # TODO : Ajouter (+=) les chaussures à Wako
    chat_wako += chaussures
    
    # # TODO : Ajouter (+=) les chaussures à Bob
    bob += chaussures

    # TODO : Ajouter (+=) le chapeau à Bob
    bob += chapeau

    # TODO: Dans une boucle, faites crier les animaux
    liste_animaux = []
    liste_animaux.append(chat_wako)
    liste_animaux.append(bob)
    liste_animaux.append(cookie)
    for animal in liste_animaux:
        print(animal.crier())
    
    # TODO : Trouver quel animal est le meilleur et son score. Afficher
    meilleur_animal_et_score = calcul_meilleur_animal(liste_animaux)
    print(meilleur_animal_et_score)

    # TODO: Créer un compte TikTok avec l'identifiant "PolyAnimalerie"
    compte_tiktok = CompteTikTok("PolyAnimalerie")

    # TODO: Créer un premier TikTok avec Wako et ajoutez le au compte
    #  Titre: "Wako est prêt pour Noël"
    #  Chanson: All I Want for Christmas is You
    #  Filtre: Ralenti
    #  UTILISEZ LES CONSTANTES DE elements_tiktok.py
    tiktok_1 = TikTok("Wako est prêt pour Noël")
    tiktok_1.musique = MUSIQUE_CHRISTMAS
    tiktok_1.filtre = FILTRE_RALENTI
    tiktok_1.ajouter_animal(chat_wako)
    
    # TODO: Créer un deuxième TikTok avec Bob et ajoutez le au compte
    #  Titre: "Bob porte un chapeau"
    #  Chanson: Bezos I
    #  Filtre: Étoiles
    #  UTILISEZ LES CONSTANTES DE elements_tiktok.py
    tiktok_2 = TikTok("Bob porte un chapeau")
    tiktok_2.musique = MUSIQUE_BEZOS_I
    tiktok_2.filtre = FILTRE_ETOILES
    tiktok_2.ajouter_animal(bob)

    # TODO: Créer un troisième TikTok avec Wako et Cookie et ajoutez le au compte
    #  Titre: "Cookie chante à Wako qui ne veut rien savoir"
    #  Chanson: September
    #  Filtre: Festif
    #  UTILISEZ LES CONSTANTES DE elements_tiktok.py
    tiktok_3 = TikTok("Cookie chante à Wako qui ne veut rien savoir")
    tiktok_3.musique = MUSIQUE_SEPTEMBER
    tiktok_3.filtre = FILTRE_FESTIF
    tiktok_3.ajouter_animal(chat_wako)
    tiktok_3.ajouter_animal(cookie)
    
    # TODO Affichez le nombre de vues du troisième TikTok
    print(tiktok_3.vues)

    # TODO: Affichez le nombre de TikTok dans le compte
    compte_tiktok += tiktok_1
    compte_tiktok += tiktok_2
    compte_tiktok += tiktok_3
    print(len(compte_tiktok))

    # TODO: Affichez le nombre total de vues du compte
    print(compte_tiktok.vues)

    # TODO: Affichez la liste des TikTok en ordre de vues
    print(compte_tiktok.tiktoks_plus_populaires())

    return compte_tiktok


if __name__ == '__main__':
    compte = main()
    for tiktok in compte.tiktoks_plus_populaires():
        print(tiktok.to_json())
