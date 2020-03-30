import unittest

from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_calc_name(self):
        calc = Calculator("My Calculator")
        self.assertEqual(calc.name, "My Calculator")

    def test_add(self):
        """Should add two digits"""
        cases = [
            {"in": (2, 2), "out": 4},
            {"in": (2, 3), "out": 5},
        ]
        for case in cases:
            self.assertEqual(self.calc.add(*case["in"]), case["out"])
    
    def test_minus(self):
        cases = [
            {"in": (2, 2), "out": 0},
            {"in": (2, 3), "out": -1},
        ]
        for case in cases:
            self.assertEqual(self.calc.minus(*case["in"]), case["out"])

    def test_sum(self):
        self.assertEqual(self.calc.sum(1, 2, 3), 6)
    
    def test_div_success(self):
        res = self.calc.div(6, 3)
        self.assertEqual(res, 2, "6 / 3 should be 2")
    
    def test_div_error(self):
        """Should raise ValueError for b == 0"""
        with self.assertRaises(ValueError):
            self.calc.div(6, 0)


if __name__ == "__main__":
    unittest.main()
