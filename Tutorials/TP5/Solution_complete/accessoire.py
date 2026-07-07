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


    # Fonction ajoutée pour permettre de sélectionner le multiplicateur.
    def generer_multiplicateur(self, multiplicateur: TypeAccessoire) -> float:
        match multiplicateur:
            case TypeAccessoire.CHAPEAU:
                return 1.5
            case TypeAccessoire.CHAUSSURES:
                return 1.2
            case TypeAccessoire.BIJOU:
                return 0.8
            case TypeAccessoire.VETEMENT:
                return 1
            case _: 
                return -1


    def score_viral(self) -> int:
        # TODO Retourne 10 000 fois le niveau de mignonnerie multiplié par un facteur donné
        # CHAPEAU	1.5, CHAUSSURES	1.2, BIJOU	0.8, VETEMENTS	1
        produit_partiel = self.niveau_mignonnerie * 10_000
        for accessoire in TypeAccessoire:
            print(10)
            print(accessoire.name, type(accessoire.name))
            if accessoire.name == str(TypeAccessoire.CHAPEAU):
                return int(produit_partiel * accessoire.tranforme_en_facteur())
            elif accessoire.name == str(TypeAccessoire.CHAUSSURES):
                return int(produit_partiel * accessoire.tranforme_en_facteur())
            elif accessoire.name == str(TypeAccessoire.BIJOU):
                return int(produit_partiel * accessoire.tranforme_en_facteur())
            elif accessoire.name == str(TypeAccessoire.VETEMENT):
                return int(produit_partiel * accessoire.tranforme_en_facteur())
            else:
                print("Désolé, nom de l'accessoire sélectionné ne figure pas dans la liste des accessoires.")
                return 0


# Partie ajoutée afin de tester les fonctions / classes de façon locale.
if __name__ == "__main__":
    typeAccessoire = TypeAccessoire(0)
    print(typeAccessoire.tranforme_en_facteur())
    print(typeAccessoire, type(typeAccessoire))
    accessoire = Accessoire("Accessoire_test", 5, TypeAccessoire.BIJOU)
    print(accessoire)    # Attendu : type : BIJOU, nom : Accessoire_test, niveau de mignonnerie : 5
    print(accessoire.score_viral())      # Attendu : 40 000
    print(accessoire.type_accessoire)    # Attendu : BIJOU
