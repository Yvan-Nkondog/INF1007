from abc import ABC
from typing import List

from animal import Animal


# TODO Je suis abstraite et j'hérite de Animal
class Oiseau(Animal, ABC):

    # TODO Implantez mon constructeur
    #  def __init__(self, ...) -> None:
    def __init__(self, nom: str, nb_pattes: int, chante: bool) -> None:
        pass
    

    def __str__(self) -> str:
        # TODO Je dois retournez une chaine de caractère semblable à :
        #  Le TYPE_OISEAU NOM_OISEAU ne chante pas.
        #  ou
        #  Le TYPE_OISEAU NOM_OISEAU chante.
        pass
       

    def crier(self) -> str:
        # TODO Je dois retourner "cuicui" si je ne chante pas.
        #  Sinon, retournez les deux premières phrases du refrain de September:
        #  Ba de ya, say that you remember. Ba de ya, dancing in September.
        pass


# TODO J'hérite de Oiseau
class Cockatiel(Oiseau):

    # TODO Implantez mon constructeur
    def __init__(self, nom: str, nb_pattes: int, chante: bool = True) -> None:
        pass
