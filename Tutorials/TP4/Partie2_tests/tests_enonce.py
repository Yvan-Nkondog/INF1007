import unittest
from unittest import TestCase
import fonctions_a_tester as fonctions


class TestFizzBuzz(TestCase):
    def test_fizz_buzz_3(self):
        # TODO Tester avec un multiple de 3

        self.assertEqual(fonctions.fizz_buzz(12), 'fizz')

    def test_fizz_buzz_5(self):
        # TODO Tester avec un multiple de 5

        self.assertEqual(fonctions.fizz_buzz(10), 'buzz')

    def test_fizz_buzz_3_5(self):
        # TODO Tester avec un multiple de 3 et 5

        self.assertEqual(fonctions.fizz_buzz(15), 'fizzbuzz')

    def test_fizz_buzz_non_facteur(self):
        # TODO Tester avec un nombre qui nombre'a pas 3 et 5 comme facteur
        #  et assurez-vous que la valeur en sotie soit une string

        self.assertEqual(fonctions.fizz_buzz(30), 'fizzbuzz')
        self.assertEqual(type(fonctions.fizz_buzz(30)), str)


class TestResoudreEquation(TestCase):
    def test_resoudre_equation_sans_racine(self):
        # TODO Tester avec un polynome sans racines réelles
        #  et assurez-vous que la valeur en sortie est None

        self.assertEqual(fonctions.resoudre_equation(1, 0, 1), None)

    def test_resoudre_equation_une_racine(self):
        # TODO Tester avec un polynome avec une seule solution

        self.assertEqual(fonctions.resoudre_equation(1, -4, 4), 2)

    def test_resoudre_equation_deux_racine(self):
        # TODO Tester avec un polynome avec deux solutions

        self.assertEqual(fonctions.resoudre_equation(1, 0, -16), (4, -4))


if __name__ == '__main__':
    unittest.main()
