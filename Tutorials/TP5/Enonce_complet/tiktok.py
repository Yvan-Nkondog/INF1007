import json
from typing import List, Union

from animal import Animal
from elements_tiktok import Musique, Filtre


class TikTok:

    # TODO Implantez mon constructeur
    def __init__(self, titre: str) -> None:
        pass

    @property
    def animaux(self):
        return self.__animaux
    
    @property
    def musique(self):
        return self.__musique
    
    @musique.setter
    def musique(self, musique: Musique):
        self.__musique = musique
    
    @property
    def filtre(self):
        return self.__filtre
    
    @filtre.setter
    def filtre(self, filtre: Filtre):
        self.__filtre = filtre

    def ajouter_animal(self, animal: Animal) -> 'TikTok':
        # TODO Ajoutez l'animal à la liste et retournez le TikTok mis à jour
        pass
    

    def __lt__(self, autre_tiktok: 'TikTok') -> bool:
        # TODO Surchargez l'opérateur < entre deux objets de type TikToks
        #  Retourne True si le présent TikTok a moins de vues que autre_tiktok
        pass

    def __str__(self) -> str:
        # TODO Je dois retournez une chaine de caractère semblable à :
        #  TITRE (NOMBRE_DE_VUES vues)
        pass

    def __repr__(self) -> str:
        return f"<{self.__str__()}>"

    @property
    def vues(self) -> int:
        # TODO Retournez le nombre de vues de votre TikTok selon la formule suivante:
        #  vues = SCORE_MUSIQUE + SCORE_FILTRE + NOMBRE_ANIMAUX* SOMME(SCORE_ANIMAUX)
        pass


    def to_json(self):
        # Ne pas modifier
        return json.dumps({
            'titre': self.titre,
            'vues': self.vues,
            'musique': self.musique.titre,
            'filtre': self.filtre.nom,
            'animaux': [
                {
                    'nom': animal.nom,
                    'espèce': type(animal).__name__,
                    'accessoires': [
                        {
                            'nom': accessoire.nom,
                            'type': str(accessoire.type_accessoire)
                        } for accessoire in animal.liste_accessoires
                    ]
                } for animal in self.__animaux
            ]
        }, ensure_ascii=False)


class CompteTikTok:

    # TODO Implantez mon constructeur
    def __init__(self, identifiant: str) -> None:
        pass

    @property
    def tiktoks(self):
        return self.__tiktoks
    

    def __len__(self) -> int:
        # TODO Surchargez l'opérateur len pour que len(COMPTE_TIKTOK) retourne le nombre de tiktok du compte
        pass

    def __iadd__(self, tiktok: TikTok) -> 'CompteTikTok':
        # TODO Surchargez l'opérateur += pour permettre d'ajouter un TikTok à la liste du compte
        #  Doit retourner le compte mis à jour
        pass

    @property
    def vues(self) -> int:
        # TODO Retourne le nombre de vues cumulatives du compte c'est à dire la somme des vues des différents TikToks
        pass

    def tiktoks_plus_populaires(self) -> List[TikTok]:
        # TODO Retourne une liste triée des TikToks du compte en ordre décroissant de vues
        # return sorted((tiktok.vues() for tiktok in self.__tiktoks), key = tiktok.vues() for tiktok in self.__tiktoks)
        pass
        