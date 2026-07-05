import math

from constantes import MASSE_VOLUMIQUE_CARBURANT, CHAMP_GRAVITATIONNEL


class Piece:
    def __init__(self, nom: str, hauteur: float, masse: float, prix: float) -> None:
        pass

    def __str__(self) -> str:
        pass


class Capsule(Piece):
    def __init__(self, nom: str, hauteur: float, masse: float, prix: float, places: int) -> None:
        pass

    def __str__(self) -> str:
        pass


class Reservoir(Piece):
    def __init__(self, nom: str, hauteur: float, masse_vide: float, prix: float, capacite: float) -> None:
        pass

    def __str__(self) -> str:
        pass

    @property
    def masse_rempli(self) -> float:
        # TODO calculez la masse du réservoir rempli.
        #  Utilisez MASSE_VOLUMIQUE_CARBURANT

        pass


class Moteur(Piece):
    def __init__(self, nom: str, hauteur: float, masse: float, prix: float, impulsion_specifique: int) -> None:
        pass

    def __str__(self) -> str:
       pass


class Fusee:

    # TODO Implanter le constructeur avec les différentes pièces comme attributs privés

    def __init__(self, nom: str, capsule: Capsule, reservoir: Reservoir, moteur: Moteur) -> None:
        pass
    

    def __str__(self) -> str:
        # TODO Implantez la fonction __str__ pour permettre l'affichage de la fusée
        pass

 
    @property
    def masse(self) -> float:
        # TODO Calculez la masse totale de la fusée (incluant le carburant)
        pass

    @property
    def hauteur(self) -> float:
        # TODO Calculez la hauteur totale de la fusée
        pass

    @property
    def prix(self) -> float:
        # TODO Calculez le prix total de la fusée
        pass

    def calculer_deltav(self) -> float:
        # TODO À partir de la masse, du moteur et du réservoir,
        #  calculez le deltaV disponible de la fusée dans l'atmosphère
        #  Utilisez la constante CHAMP_GRAVITATIONNEL
        pass


if __name__ == '__main__':
    # Reservoir.masse_rempli
    reservoir = Reservoir("Pichet", 0.4, 0.5, 20, 2)
    masse_rempli = reservoir.masse_rempli
    print(f"Une fois rempli, {reservoir.nom} a une masse de {masse_rempli} kg")
    print()

    # Fusee constructeur
    capsule = Capsule("Exigüe", 1.0, 750, 1300.0, 1)
    reservoir = Reservoir("Pichet", 0.4, 0.5, 20.0, 2)
    moteur = Moteur("Pantera Arctic Cat Triple 800", 4, 2000, 14000.0, 199)
    fusee = Fusee("Romano Fafard", capsule, reservoir, moteur)

    # Fusee.masse
    print(f"La masse de la fusée {fusee.nom} est {fusee.masse}kg")
    print()

    # Fusee.hauteur
    print(f"La hauteur de la fusée {fusee.nom} est {fusee.hauteur}m")
    print()

    # Fusee.prix
    print(f"Le prix de la fusée {fusee.nom} est {fusee.prix}$")
    print()

    # Fusee.__str__
    print(f"fusee est de type {type(fusee)}")
    print()
