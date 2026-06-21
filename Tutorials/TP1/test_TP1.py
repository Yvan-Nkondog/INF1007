
from exercice1 import fizzBuzz
from exercice2 import resoudreEquation
from exercice3 import decomposer
from exercice4 import calculerPosition
from exercice5 import pointDeRencontre
from exercice6 import effectuerRotation
from exercice6 import trouverModule
import unittest
import os
import sys
class Exo1Tests(unittest.TestCase):
    def testMultiple3(self):
        try:
            self.assertEqual(fizzBuzz(9).lower(), "fizz")
            self.assertEqual(fizzBuzz(42).lower(), "fizz")
            self.assertEqual(fizzBuzz(9).lower(), "fizz")
        finally:
            pass
    def testMultiple5(self):
        try:
            self.assertEqual(fizzBuzz(95).lower(), "buzz")
            self.assertEqual(fizzBuzz(5).lower(), "buzz")
            self.assertEqual(fizzBuzz(20).lower(), "buzz")
        finally:
            pass
    def testMultiple5et3(self):
        try:
            self.assertEqual(fizzBuzz(15).lower(), "fizzbuzz")
            self.assertEqual(fizzBuzz(60).lower(), "fizzbuzz")
            self.assertEqual(fizzBuzz(135).lower(), "fizzbuzz")
        finally:
            pass

class Exo2Tests(unittest.TestCase):
    def testSansRacine(self):
        try:
            self.assertEqual(resoudreEquation(9,2,5), None )
            self.assertEqual(resoudreEquation(-3, 1, -3), None)
            self.assertEqual(resoudreEquation(1,1,5), None)
        finally:
            pass
    def testUneRacine(self):
        try:
            self.assertEqual(int(resoudreEquation(30,0,0)), 0 )
            self.assertEqual(int(resoudreEquation(2, 4, 2)), -1)
        finally:
            pass
    def testDeuxRacines(self):
        try:
            x1 = min(resoudreEquation(30,50,20))
            x2 = max(resoudreEquation(30,50,20))
            self.assertAlmostEqual(x1,-1, None, None, 0.002)
            self.assertAlmostEqual(x2,-0.666, None, None, 0.002)
            x1 = min(resoudreEquation(1,-2,-15))
            x2 = max(resoudreEquation(1,-2,-15))
            self.assertAlmostEqual(x1,-3, None, None, 0.002)
            self.assertAlmostEqual(x2,5, None, None, 0.002)
            x1 = min(resoudreEquation(1,1,-2))
            x2 = max(resoudreEquation(1,1,-2))
            self.assertAlmostEqual(x1,-2, None, None, 0.002)
            self.assertAlmostEqual(x2,1, None, None, 0.002)
        finally:
            pass

class Exo3Tests(unittest.TestCase):
    def test1(self):
        try:
            self.assertEqual(decomposer(27882), (0, 0, 0, 7, 44, 42) )
        finally:
            pass
    def test2(self):
        try:
            self.assertEqual(decomposer(98675437338), (3128, 50, 6, 19, 42, 18) )
        finally:
            pass

    def test3(self):
        try:
            self.assertEqual(decomposer(37827382764), (1199, 25, 6, 22, 19, 24))
        finally:
            pass

    def test4(self):
        try:
            self.assertEqual(decomposer(222), (0, 0, 0, 0, 3, 42))
        finally:
            pass

class Exo4Tests(unittest.TestCase):
    def testPosition1(self):
        try:
            self.assertAlmostEqual(calculerPosition(0, 18, 22,98), 354.444, None, None, 0.002)
        finally:
            pass
    def testPosition2(self):
        try:
            self.assertAlmostEqual(calculerPosition(0, 200, 1020,88), 40800, None, None, 0.002)
        finally:
            pass
    def testPosition3(self):
        try:
            self.assertAlmostEqual(calculerPosition(300, 10,22 ,55), 498.61, None, None, 0.002)
        finally:
            pass


class Exo5Tests(unittest.TestCase):
    def testPointDeRencontre1(self):
        try:
            self.assertAlmostEqual(pointDeRencontre(40,60,81),32.400000000000006, None, None, 0.002)
        finally:
            pass

    def testPointDeRencontre2(self):
        try:
            self.assertAlmostEqual(pointDeRencontre(120,60,5),3.3333, None, None, 0.002)
        finally:
            pass

    def testPointDeRencontre3(self):
        try:
            self.assertAlmostEqual(pointDeRencontre(0,5,7),0, None, None, 0.002)
        finally:
            pass

class Exo6Tests(unittest.TestCase):
    def testModule1(self):
        try:
            self.assertAlmostEqual(trouverModule(complex(1,7)),7.071, None, None, 0.002)
        finally:
            pass

    def testModule2(self):
        try:
            self.assertAlmostEqual(trouverModule(complex(-11,7)),13.0384, None, None, 0.002)
        finally:
            pass

    def testEffectuerRotation1(self):
        try:
            self.assertAlmostEqual(effectuerRotation(complex(2,2), 0, trouverModule),complex(2,2), None, None, 0.002)
        finally:
            pass

    def testEffectuerRotation2(self):
        try:
            resultat = effectuerRotation(complex(2, 2), 19, trouverModule)
            self.assertAlmostEqual(resultat.real,1.23990, None, None, 0.002)
            self.assertAlmostEqual(resultat.imag,2.542173, None, None, 0.002)
        finally:
            pass
    def testEffectuerRotation3(self):
        try:
            resultat = effectuerRotation(complex(8, 12), 144, trouverModule)
            self.assertAlmostEqual(resultat.real,6, None, None, 0.002)
            self.assertAlmostEqual(resultat.imag,2.542173, None, None, 0.002)
        except:
            pass
    def testEffectuerRotation4(self):
        try:
            resultat = effectuerRotation(complex(-6, -18), 900, trouverModule)
            self.assertAlmostEqual(resultat.real,6, None, None, 0.002)
            self.assertAlmostEqual(resultat.imag,18, None, None, 0.002)
        finally:
            pass
    def testEffectuerRotation5(self):
        try:
            resultat = effectuerRotation(complex(-2, 19), -90, trouverModule)
            self.assertAlmostEqual(resultat.real,19, None, None, 0.002)
            self.assertAlmostEqual(resultat.imag,2, None, None, 0.002)
        finally:
            pass

if __name__ == '__main__':
    if not os.path.exists('logs'):
        os.mkdir('logs')
    with open('./correction.txt', 'w') as f:
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(sys.modules[__name__])
        unittest.TextTestRunner(f, verbosity=2).run(suite)
