import unittest
from catalan_numbers import catalan_numbers_gen
from collections.abc import Generator
from functools import reduce

class TestCatalan(unittest.TestCase):
    def test_generator(self):
        sequence = catalan_numbers_gen()
        self.assertIsInstance(sequence, Generator)

        self.assertEqual(next(sequence), 1)
        self.assertEqual(next(sequence), 1)
        self.assertEqual(next(sequence), 2)

    def test_sequence(self):
        gen = catalan_numbers_gen()
        sequence = [next(gen) for _ in range(10)]
        self.assertEqual(len(sequence), 10)
        self.assertListEqual(sequence, [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862])

        exp = [16796, 58786]
        for ind, val in enumerate(gen):
            if ind > 1:
                break
            self.assertEqual(val, exp[ind])

    def test_func(self):
        gen = catalan_numbers_gen()
        sequence = list(zip(range(5), gen))
        self.assertEqual(len(sequence), 5)
        self.assertListEqual(sequence, [(0, 1), (1, 1), (2, 2), (3, 5), (4, 14)])

        sequence = list(zip(range(5), gen))
        self.assertEqual(len(sequence), 5)
        self.assertListEqual(sequence, [(0, 42), (1, 132), (2, 429), (3, 1430), (4, 4862)])


if __name__ == "__main__":
    unittest.main()
