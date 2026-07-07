from abc import ABC
from typing import List

from animal import Animal


# TODO Je suis abstraite et j'hérite de Animal
class Reptile(Animal, ABC):

    # TODO Implantez mon constructeur
    def __init__(self, nom: str, nb_pattes, est_nocture: bool) -> None:
        pass


    def __str__(self) -> str:
        # TODO Je dois retournez une chaine de caractère semblable à :
        #  Le TYPE_REPTILE NOM_REPTILE est nocturne.
        #  ou
        #  Le TYPE_REPTILE NOM_REPTILE est diurne.
        pass



# TODO J'hérite de Reptile
class Serpent(Reptile):

    # TODO Implantez mon constructeur
    def __init__(self, nom, est_nocture: bool, est_venimeux: bool) -> None:
        pass

    def __str__(self) -> str:
        super(Serpent, self).__str__()
        # TODO Ajouter les phrases suivantes à la chaine de base de Reptile:
        #  Il est venimeux.
        #  ou
        #  Il n'est pas venimeux.
        #  Utilisez la methode __str__ de Reptile avec: super(Serpent, self).__str__()
        pass

    def crier(self) -> str:
        # TODO Retournez le cri du serpent: sssss
        pass
