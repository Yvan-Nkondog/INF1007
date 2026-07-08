from abc import ABC, abstractmethod


# TODO Je suis abstraite
class ElementViral(ABC):

    # Cette méthode rend la classe ElementViral abstraite 
    # et doit être implémentée par toutes les classes filles.
    @abstractmethod
    def score_viral(self) -> int:
        # TODO Rendez-moi abstraite
        pass


# TODO J'hérite de ElementViral
class Musique(ElementViral):

    # TODO Implanter mon constructeur

    def __init__(self, titre: str, nb_ecoutes: int) -> None:
        self.titre = titre
        self.nb_ecoutes = nb_ecoutes

    def score_viral(self) -> int:
        # TODO Le score est le nombre d'écoutes divisé par 10 000
        return int(self.nb_ecoutes / 10_000)


# TODO J'hérite de ElementViral
class Filtre(ElementViral):

    # TODO Implanter mon constructeur
    def __init__(self, nom: str, nb_utilisations: int) -> None:
        self.nom = nom
        self.nb_utilisations = nb_utilisations

    def score_viral(self) -> int:
        # TODO Le score est le d'utilisations divisé par 50 000
        return int(self.nb_utilisations / 50_000)


FILTRE_RALENTI = Filtre("Ralenti", 50000000)
FILTRE_ETOILES = Filtre("Étoiles", 500000)
FILTRE_FESTIF = Filtre("Festif", 1000000)

MUSIQUE_CHRISTMAS = Musique("All I Want for Christmas is You", 934220516)
MUSIQUE_BEZOS_I = Musique("Bezos I", 95610379)
MUSIQUE_SEPTEMBER = Musique("September", 941627159)
