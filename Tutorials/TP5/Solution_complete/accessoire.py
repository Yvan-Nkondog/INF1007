from enum import Enum

from elements_tiktok import ElementViral


class TypeAccessoire(Enum):
    CHAPEAU = 0
    CHAUSSURES = 1
    BIJOU = 2
    VETEMENT = 3

    def __str__(self):
        return self.name
    

    # Fonction ajoutée pour permettre de retourner les facteurs.
    def tranforme_en_facteur(self) -> float:
        #Retourne le facteur correspondant à la valeur 'enum'.
        dictionnaire_facteur = {
            TypeAccessoire.CHAPEAU: 1.5,
            TypeAccessoire.CHAUSSURES: 1.2,
            TypeAccessoire.BIJOU: 0.8,
            TypeAccessoire.VETEMENT: 1
        }
        return dictionnaire_facteur[self]


# TODO J'hérite de ElementViral
class Accessoire(ElementViral):

    # TODO Implantez mon constructeur
    def __init__(self, nom: str, niveau_mignonnerie: int, type_accessoire: TypeAccessoire) -> None:
        self.__type_accessoire = type_accessoire
        self.nom = nom
        self.niveau_mignonnerie = niveau_mignonnerie
        

    @property
    def type_accessoire(self):
        return self.__type_accessoire


    def __str__(self) -> str:
        # TODO Je dois retournez une chaine de caractère semblable à :
        #  type : TYPE_ACCESSOIRE, nom : NOM_ACCESSOIRE, niveau de mignonnerie : NIVEAU_DE_MIGNONNERIE
        #  TypeAccessoire a déjà une implantation de __str__. Utilisez-là!
        return (
            f"type : {self.__type_accessoire.__str__()}, "
            f"nom : {self.nom}, "
            f"niveau de mignonnerie : {self.niveau_mignonnerie}"
        )


    def __repr__(self) -> str:
        return f"<{self.__str__()}>"


    def score_viral(self) -> int:
        # TODO Retourne 10 000 fois le niveau de mignonnerie multiplié par un facteur donné
        # CHAPEAU	1.5, CHAUSSURES	1.2, BIJOU	0.8, VETEMENTS	1
        produit_partiel = self.niveau_mignonnerie * 10_000
        match(self.type_accessoire):
            case TypeAccessoire.CHAPEAU:
                return int(produit_partiel * self.type_accessoire.tranforme_en_facteur())
            case TypeAccessoire.CHAUSSURES:
                return int(produit_partiel * self.type_accessoire.tranforme_en_facteur())
            case TypeAccessoire.BIJOU:
                return int(produit_partiel * self.type_accessoire.tranforme_en_facteur())
            case TypeAccessoire.VETEMENT:
                return int(produit_partiel * self.type_accessoire.tranforme_en_facteur())
            case _:
                print("Désolé, nom de l'accessoire sélectionné ne " \
                "figure pas dans la liste des accessoires.")
                return 0
