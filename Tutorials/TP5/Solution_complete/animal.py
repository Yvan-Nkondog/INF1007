from abc import abstractmethod, ABC
from typing import List, Tuple

from accessoire import Accessoire, TypeAccessoire
from elements_tiktok import ElementViral


# TODO Je suis abstraite et j'hérite de ElementViral
class Animal(ElementViral, ABC):

    # TODO Implantez mon constructeur
    def __init__(self, nom: str, nb_pattes: int) -> None:
        self.nom = nom
        self.nb_pattes = nb_pattes
        self.liste_accessoires: List[Accessoire] = []


    def __add__(self, accessoire: Accessoire) -> int:
        # TODO Retournez le score viral de l'animal plus celui de l'accessoire
        return self.score_viral() + accessoire.score_viral()


    def __iadd__(self, accessoire: Accessoire) -> 'Animal':
        # TODO Ajoutez l'accessoire à la liste de l'animal. Retournez l'animal en question
        #  Attention! Un animal n'ayant aucune patte ne peut enfiler des chaussures
        message_si_sans_pattes = f"Désolé, un animal de type {self.__class__.__name__} n'a "
        f"pas de pattes et ne peux donc pas porter de chaussures."
        if self.nb_pattes == 0:
            print(message_si_sans_pattes)
            return self
        self.liste_accessoires.append(accessoire)
        return self

    @abstractmethod
    def crier(self) -> str:
        # TODO Rendez-moi abstraite
        pass


    def score_viral(self) -> int:
        # TODO Retournez la somme du score viral des accessoires présents dans la liste d'accessoires de l'animal
        for accessoire in self.liste_accessoires:
            print(accessoire.score_viral())
        return sum([accessoire.score_viral() for accessoire in self.liste_accessoires])


def calcul_meilleur_animal(animaux: List[Animal]) -> Tuple[str, int]:
    # TODO Retournez le nom et le score viral de l'animal ayant le score le plus haut
    return max([(animaux[i].nom, animaux[i].score_viral()) for i in range(len(animaux))], key=lambda animal: animal[1])
