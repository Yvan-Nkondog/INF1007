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
    

    # TODO : Afficher Wako
    

    # TODO : Creer un objet Serpent qui s'appelle Bob, qui est diurne et qui n'est pas venimeux
    

    # TODO : Afficher Bob
    


    # TODO : Creer un objet Cockatiel qui s'appelle Cookie avec 2 pattes
    

    # TODO : Afficher cookie
    


    # TODO : Creer un objet Accessoire de type chapeau avec un niveau de mignonnerie de 4
    

    # TODO : Creer un objet Accessoire de type chaussures avec un niveau de mignonnerie de 6
    

    # TODO : Ajouter (+=) les chaussures à Wako
    


    # TODO : Ajouter (+=) les chaussures à Bob
    


    # TODO : Ajouter (+=) le chapeau à Bob
    

    
    # TODO: Dans une boucle, faites crier les animaux
    
    

    # TODO : Trouver quel animal est le meilleur et son score. Afficher
    

    # TODO: Créer un compte TikTok avec l'identifiant "PolyAnimalerie"
    

    # TODO: Créer un premier TikTok avec Wako et ajoutez le au compte
    #  Titre: "Wako est prêt pour Noël"
    #  Chanson: All I Want for Christmas is You
    #  Filtre: Ralenti
    #  UTILISEZ LES CONSTANTES DE elements_tiktok.py
    


    # TODO: Créer un deuxième TikTok avec Bob et ajoutez le au compte
    #  Titre: "Bob porte un chapeau"
    #  Chanson: Bezos I
    #  Filtre: Étoiles
    #  UTILISEZ LES CONSTANTES DE elements_tiktok.py
    

    # TODO: Créer un troisième TikTok avec Wako et Cookie et ajoutez le au compte
    #  Titre: "Cookie chante à Wako qui ne veut rien savoir"
    #  Chanson: September
    #  Filtre: Festif
    #  UTILISEZ LES CONSTANTES DE elements_tiktok.py
    
    
    # TODO Affichez le nombre de vues du troisième TikTok
    

    # TODO: Affichez le nombre de TikTok dans le compte
    

    # TODO: Affichez le nombre total de vues du compte
    

    # TODO: Affichez la liste des TikTok en ordre de vues
    

    pass


if __name__ == '__main__':
    compte = main()
    for tiktok in compte.tiktoks_plus_populaires():
        print(tiktok.to_json())
