
import math

from constantes import MASSE_VOLUMIQUE_CARBURANT, CHAMP_GRAVITATIONNEL


class Piece:
    def __init__(self, nom: str, hauteur: float, masse: float, prix: float) -> None:
        self.nom = nom
        self.hauteur = hauteur
        self.masse = masse
        self.prix = prix

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}:\n"
            f"\tnom: {self.nom}\n"
            f"\thauteur: {self.hauteur}\n"
            f"\tmasse: {self.masse}\n"
            f"\tprix: {self.prix}\n"
        )


class Capsule(Piece):
    def __init__(self, nom: str, hauteur: float, masse: float, prix: float, places: int) -> None:
        super().__init__(nom, hauteur, masse, prix)
        self.places = places

    def __str__(self) -> str:
        return super().__str__() + f"\tplaces: {self.places}\n"


class Reservoir(Piece):
    def __init__(self, nom: str, hauteur: float, masse_vide: float, prix: float, capacite: float) -> None:
        super().__init__(nom, hauteur, masse_vide, prix)
        self.capacite = capacite

    def __str__(self) -> str:
        return super().__str__() + f"\tcapacite : {self.capacite}\n"

    @property
    def masse_rempli(self) -> float:
        # TODO calculez la masse du réservoir rempli.
        #  Utilisez MASSE_VOLUMIQUE_CARBURANT
        masse_carburant = self.capacite * MASSE_VOLUMIQUE_CARBURANT
        return self.masse + masse_carburant


class Moteur(Piece):
    def __init__(self, nom: str, hauteur: float, masse: float, prix: float, impulsion_specifique: int) -> None:
        super().__init__(nom, hauteur, masse, prix)
        self.impulsion_specifique = impulsion_specifique

    def __str__(self) -> str:
       return super().__str__() + f"impulsion_specifique: {self.impulsion_specifique}\n"


class Fusee:

    # TODO Implanter le constructeur avec les différentes pièces comme attributs privés

    def __init__(self, nom: str, capsule: Capsule, reservoir: Reservoir, moteur: Moteur) -> None:
        self.nom = nom
        self.__capsule = capsule
        self.__reservoir = reservoir
        self.__moteur = moteur
    
    def __str__(self) -> str:
        # TODO Implantez la fonction __str__ pour permettre l'affichage de la fusée
        return (
            f'Fusée:\n'
            f'\tNom: {self.nom}\n'
            f'\tHauteur totale: {self.hauteur}m\n'
            f'\tMasse totale (remplie): {self.masse}kg\n'
            f'\tPrix total: {self.prix}$\n'
            f'Pièces:\n'
            f'\tCapsule: {self.__capsule.nom}, hauteur={self.__capsule.hauteur}m, '
            f'masse={self.__capsule.masse}kg, prix={self.__capsule.prix}$, '
            f'places={self.__capsule.places} personne(s)\n'
            f'\tRéservoir: {self.__reservoir.nom}, hauteur={self.__reservoir.hauteur}m, '
            f'masse={self.__reservoir.masse}kg, prix={self.__reservoir.prix}$, '
            f'capacité={self.__reservoir.capacite}L\n'
            f'\tMoteur: {self.__moteur.nom}, hauteur={self.__moteur.hauteur}m, '
            f'masse={self.__moteur.masse}kg, prix={self.__moteur.prix}$, '
            f'impulsion spécifique={self.__moteur.impulsion_specifique}s'
        )

    @property
    def masse(self) -> float:
        # TODO Calculez la masse totale de la fusée (incluant le carburant)
        return self.__capsule.masse + self.__reservoir.masse_rempli + self.__moteur.masse

    @property
    def hauteur(self) -> float:
        # TODO Calculez la hauteur totale de la fusée
        return self.__capsule.hauteur + self.__reservoir.hauteur + self.__moteur.hauteur

    @property
    def prix(self) -> float:
        # TODO Calculez le prix total de la fusée
        return self.__capsule.prix + self.__reservoir.prix + self.__moteur.prix
    
    def calculer_deltav(self) -> float:
        # TODO À partir de la masse, du moteur et du réservoir,
        #  calculez le deltaV disponible de la fusée dans l'atmosphère
        #  Utilisez la constante CHAMP_GRAVITATIONNEL
        masse_vide_fusee = self.masse - (self.__reservoir.capacite * MASSE_VOLUMIQUE_CARBURANT)
        return (
            self.__moteur.impulsion_specifique * CHAMP_GRAVITATIONNEL * 
            math.log(self.masse / masse_vide_fusee)
        )


if __name__ == '__main__':
    # Reservoir.masse_rempli
    reservoir = Reservoir("Pichet", 0.4, 0.5, 20, 2)
    masse_rempli = reservoir.masse_rempli
    print(f"Une fois rempli, {reservoir.nom} a une masse de {masse_rempli} kg")
    print()
    print(reservoir)

    # Fusee constructeur
    capsule = Capsule("Exigüe", 1.0, 750, 1300.0, 1)
    reservoir = Reservoir("Pichet", 0.4, 0.5, 20.0, 2)
    moteur = Moteur("Pantera Arctic Cat Triple 800", 4, 2000, 14000.0, 199)
    fusee = Fusee("Romano Fafard", capsule, reservoir, moteur)
    print(capsule)

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

    delta_v = fusee.calculer_deltav()
    print(f"Le deltaV de la fusée {fusee.nom} est {delta_v:.2f}m/s")
