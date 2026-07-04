import unittest
from unittest import TestCase
import fonctions_a_tester as fonctions


class TestFizzBuzz(TestCase):
    def test_fizz_buzz_3(self):
        # TODO Tester avec un multiple de 3
        message = "Tester avec un multiple de 3"
        self.assertEqual(fonctions.fizz_buzz(27).lower(), "fizz", message)


    def test_fizz_buzz_5(self):
        message = "Tester avec un multiple de 3"
        # TODO Tester avec un multiple de 5
        self.assertEqual(fonctions.fizz_buzz(25).lower(), "buzz", message)

    def test_fizz_buzz_3_5(self):
        # TODO Tester avec un multiple de 3 et 5
        message = "Tester avec un multiple commun à 3 et 5"
        self.assertEqual(fonctions.fizz_buzz(15).lower(), "fizzbuzz", message)                                                                                                                                                                                                                                                                                                                                         

    def test_fizz_buzz_non_facteur(self):
        # TODO Tester avec un nombre qui n'a pas 3 et 5 comme facteur
        #  et assurez-vous que la valeur en sotie soit une string
        message_sans_facteur = "Tester avec un nombre qui n'a pas 3 et 5 comme facteur"
        message_type = "La valeur de sortie doit être une 'string, str'"
        self.assertEqual(fonctions.fizz_buzz(17), str(17), message_sans_facteur)
        self.assertIsInstance(fonctions.fizz_buzz(17), str, message_type)


class TestResoudreEquation(TestCase):
    def test_resoudre_equation_sans_racine(self):
        # TODO Tester avec un polynome sans racines réelles
        #  et assurez-vous que la valeur en sortie est None
        message = "La valeur de retour doit être 'None' parce que le polynôme n'a pas de racine réelle."
        self.assertEqual(fonctions.resoudre_equation(1, -4, 5), None, )       

    def test_resoudre_equation_une_racine(self):
        # TODO Tester avec un polynome avec une seule solution
        message = "Le test prévoit une seule solution pour cette combinaison de valeurs d'entrée."
        self.assertAlmostEqual(fonctions.resoudre_equation(3, -6, 3), 1, message)
        self.assertAlmostEqual(fonctions.resoudre_equation(3, 6, 3), -1, message)
        self.assertAlmostEqual(fonctions.resoudre_equation(7, 0, 0), 0, message)
        
    def test_resoudre_equation_deux_racine(self):
        # TODO Tester avec un polynome avec deux solutions
        message = "Le test prévoit que la combinaison en entrée génère deux racines en sortie."
        delta = 0.002

        x1 = min(fonctions.resoudre_equation(3, -5, -2))
        x2 = max(fonctions.resoudre_equation(3, -5, -2))
        self.assertAlmostEqual(x1, -1/3, None, message, delta)
        self.assertAlmostEqual(x2, 2, None, message, delta)
        
        x1 = min(fonctions.resoudre_equation(1, 3, 2))
        x2 = max(fonctions.resoudre_equation(1, 3, 2))
        self.assertAlmostEqual(x1, -2, None, message, delta)
        self.assertAlmostEqual(x2, -1, None, message, delta)

        x1 = min(fonctions.resoudre_equation(1, -5, 3))
        x2 = max(fonctions.resoudre_equation(1, -5, 3))
        self.assertAlmostEqual(x1, 0.698, None, message, delta)
        self.assertAlmostEqual(x2, 4.302, None, message, delta)

     
if __name__ == '__main__':
    unittest.main()
