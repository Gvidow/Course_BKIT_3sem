import unittest.mock
from BiSquareRoot import BiSquareRoot, read_factors
import sys


def compare_list(lst1, lst2):
    return len(lst1) == len(lst2) and set(lst1) == set(lst2)


class TestBiSquareRoot(unittest.TestCase):
    def test_calculate(self):
        tests = [
            ([5, -5, 0], [1, -1, 0]),
            ([1, 1, 9], []),
            ([-5, -2, -34], []),
            ([5, 34, 12], []),
            ([113, 23, 1], []),
            ([-1, -1, -11], []),
            ([1, -25, 144], [3, -3, 4, -4]),
            ([1, -8, 16], [2, -2]),
            ([0.01, -0.0769, 0.09], [-1.2, 1.2, -2.5, 2.5]),
            ([1, -7.69, 9], [-1.2, 1.2, -2.5, 2.5]),
            ([50, 550, -2306.88], [-1.8, 1.8]),
            ([500, 5500, -23068.8], [-1.8, 1.8]),
        ]
        for test in tests:
            equation = BiSquareRoot(*test[0])
            res = equation.calculate()
            self.assertTrue(compare_list(res, test[1]))


class TestMain(unittest.TestCase):
    @unittest.mock.patch("BiSquareRoot.input")
    def test_read_factors(self, input_mock):
        sys.argv.extend("2 sdgg sd / -26 ds".split())
        input_mock.return_value = "12.7"
        self.assertEqual(read_factors(), [2, -26, 12.7])

        sys.argv.append("18")
        self.assertEqual(read_factors(), [2, -26, 18])
        sys.argv = sys.argv[:1]


if __name__ == "__main__":
    unittest.main()
