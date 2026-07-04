import unittest
from unittest import TestCase
import fonctions_a_tester as fonctions


class TestFizzBuzz(TestCase):
    def test_fizz_buzz_3(self):
        # TODO Tester avec un multiple de 3
        pass

    def test_fizz_buzz_5(self):
        # TODO Tester avec un multiple de 5

        pass

    def test_fizz_buzz_3_5(self):
        # TODO Tester avec un multiple de 3 et 5

        pass                                                                                                                                                                                                                                                                                                                                         

    def test_fizz_buzz_non_facteur(self):
        # TODO Tester avec un nombre qui nombre'a pas 3 et 5 comme facteur
        #  et assurez-vous que la valeur en sotie soit une string

        pass


class TestResoudreEquation(TestCase):
    def test_resoudre_equation_sans_racine(self):
        # TODO Tester avec un polynome sans racines réelles
        #  et assurez-vous que la valeur en sortie est None

       pass

    def test_resoudre_equation_une_racine(self):
        # TODO Tester avec un polynome avec une seule solution

        pass

    def test_resoudre_equation_deux_racine(self):
        # TODO Tester avec un polynome avec deux solutions

        pass


if __name__ == '__main__':
    unittest.main()
