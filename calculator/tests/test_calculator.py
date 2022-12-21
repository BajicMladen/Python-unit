from calculator.app.calculator import Calculator
import unittest

NUMBER_1 = 3.0
NUMBER_2 = 2.0
FAILURE = 'Test Failed'


class CalculatorTest(unittest.TestCase):
  # SetUp metoda koja se pokrece prje svakog testa
    def setUp(self):
        self.calc = Calculator()

    # Testiranje inicijalne vrijednosti atributa objekta
    def test_last_answer_init(self):
        value = self.calc.last_answer
        self.assertEqual(value, 0.0, FAILURE) 

    # Test za metodu - add() koja sabira dva broja
    def test_add(self):
        value = self.calc.add(NUMBER_1, NUMBER_2)
        self.assertEqual(value, 5.0, FAILURE)
        self.assertEqual(value, self.calc.last_answer, FAILURE)

    # Test za metodu - subtract() koja oduzima dva broja
    def test_subtract(self):
        value = self.calc.subtract(NUMBER_1, NUMBER_2)
        self.assertEqual(value, 1.0, FAILURE)
        self.assertEqual(value, self.calc.last_answer, FAILURE)

     # Test za metodu - subtract() ali kada je rezultat negativan broj
    def test_subtract_negative(self):
        value = self.calc.subtract(NUMBER_2, NUMBER_1)
        self.assertEqual(value, -1.0, FAILURE)
        self.assertEqual(value, self.calc.last_answer, FAILURE)

    # Test za metodu - mulitpy() koja mnozi dva broja
    def test_multiply(self):
        value = self.calc.multiply(NUMBER_1, NUMBER_2)
        self.assertEqual(value, 6.0, FAILURE)
        self.assertEqual(value, self.calc.last_answer, FAILURE)

    # Test za metodu - devide() koja dijeli dva broja
    def test_divide(self):
        value = self.calc.divide(NUMBER_1, NUMBER_2)
        self.assertEqual(value, 1.5, FAILURE)
        self.assertEqual(value, self.calc.last_answer, FAILURE)

    # Test za metodu - devide() koja dijeli dva broja - kada je drugi broj nula
    def test_divide_by_zero(self):
        self.assertRaises(ZeroDivisionError, self.calc.divide, NUMBER_1, 0)

    # Test za metodu - maximum() koja poredi dva broja i vraca veci - ukoliko su isti - vraca prvi broj
    def test_max_greater(self):
        value = self.calc.maximum(NUMBER_1, NUMBER_2)
        self.assertEqual(value, NUMBER_1, FAILURE)
        self.assertEqual(value, self.calc.last_answer, FAILURE)

    # Test za metodu - maximum() koja poredi dva broja i vraca veci - ukoliko su isti - vraca prvi broj
    def test_max_less(self):
        value = self.calc.maximum(NUMBER_2, NUMBER_1)
        self.assertEqual(value, NUMBER_1, FAILURE)
        self.assertEqual(value, self.calc.last_answer, FAILURE)

    # Test za metodu - maximum() koja poredi dva broja i vraca veci - ukoliko su isti - vraca prvi broj
    def test_max_equal(self):
        value = self.calc.maximum(NUMBER_1, NUMBER_1)
        self.assertEqual(value, NUMBER_1, FAILURE)
        self.assertEqual(value, self.calc.last_answer, FAILURE)

    # Test za metodu - mimimum() koja poredi dva broja i vraca manji - ukoliko su isti - vraca prvi broj
    def test_min_greater(self):
        value = self.calc.minimum(NUMBER_1, NUMBER_2)
        self.assertEqual(value, NUMBER_2, FAILURE)
        self.assertEqual(value, self.calc.last_answer, FAILURE)

    # Test za metodu - mimimum() koja poredi dva broja i vraca manji - ukoliko su isti - vraca prvi broj
    def test_min_less(self):
        value = self.calc.minimum(NUMBER_2, NUMBER_1)
        self.assertEqual(value, NUMBER_2, FAILURE)
        self.assertEqual(value, self.calc.last_answer, FAILURE)

    # Test za metodu - mimimum() koja poredi dva broja i vraca manji - ukoliko su isti - vraca prvi broj
    def test_min_equal(self):
        value = self.calc.minimum(NUMBER_2, NUMBER_2)
        self.assertEqual(value, NUMBER_2, FAILURE)
        self.assertEqual(value, self.calc.last_answer, FAILURE)