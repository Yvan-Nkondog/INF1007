from abc import ABC
from enum import Enum
from typing import List

from animal import Animal, calcul_meilleur_animal
from accessoire import Accessoire, TypeAccessoire


class LongueurPoils(Enum):
    RASES = 0
    COURTS = 1
    LONGS = 2

    def __str__(self):
        return self.name


# TODO Je suis abstraite et j'hérite de Animal

class Mammifere(Animal, ABC):

    # TODO Implantez mon constructeur
    def __init__(self, nom: str, nb_pattes: int, longeur_poils: LongueurPoils) -> None:
        super().__init__(nom, nb_pattes)
        self.longueur_poils = longeur_poils


    def __str__(self) -> str:
        # TODO Je dois retournez une chaine de caractère semblable à :
        #  Le TYPE_MAMMIFERE NOM_MAMMIFERE a NB_PATTES pattes et des poils LONGUEUR_POILS.
        return (
            f"Le {self.__class__.__name__} {self.nom} a "
            f"{self.nb_pattes} pattes et des poils {self.longueur_poils.__str__()}."
        )


# TODO J'hérite de Mammifere
class Chat(Mammifere):

    # TODO Implantez mon constructeur
    #  def __init__(self, ...) -> None:
    def __init__(self, nom, longueur_poils: LongueurPoils, couleur: str) -> None:
        super().__init__(nom, 4, longueur_poils)  # Le chat possède 4 pattes par défaut.
        self.couleur = couleur


    def crier(self) -> str:
        # TODO Retournez le cri du chat: Miaou
        return "Miaou"
