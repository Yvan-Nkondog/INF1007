from abc import ABC
from typing import List

from animal import Animal


# TODO Je suis abstraite et j'hérite de Animal
class Reptile(Animal, ABC):

    # TODO Implantez mon constructeur
    def __init__(self, nom: str, nb_pattes, est_nocture: bool) -> None:
        super().__init__(nom, nb_pattes) 
        self.est_nocturne = est_nocture


    def __str__(self) -> str:
        # TODO Je dois retournez une chaine de caractère semblable à :
        #  Le TYPE_REPTILE NOM_REPTILE est nocturne.
        #  ou
        #  Le TYPE_REPTILE NOM_REPTILE est diurne.
        if self.est_nocturne == True:
            return f"Le {self.__class__.__name__} {self.nom} est nocturne."
        return f"Le {self.__class__.__name__} {self.nom} est diurne."


# TODO J'hérite de Reptile
class Serpent(Reptile):

    # TODO Implantez mon constructeur
    def __init__(self, nom, est_nocture: bool, est_venimeux: bool) -> None:
        super().__init__(nom, 0, est_nocture)
        self.est_venimeux = est_venimeux


    def __str__(self) -> str:
        chaine_classe_serpent = super(Serpent, self).__str__()
        # TODO Ajouter les phrases suivantes à la chaine de base de Reptile:
        #  Il est venimeux.
        #  ou
        #  Il n'est pas venimeux.
        #  Utilisez la methode __str__ de Reptile avec: super(Serpent, self).__str__()
        if self.est_venimeux == True:
            return chaine_classe_serpent + " Il est venimeux."
        return chaine_classe_serpent + " Il n'est pas venimeux."


    def crier(self) -> str:
        # TODO Retournez le cri du serpent: sssss
        return "sssss"
